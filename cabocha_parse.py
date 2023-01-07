import sys
from cabocha.analyzer import CaboChaAnalyzer
from functional import seq

analyzer = CaboChaAnalyzer()


def parse_sentence(sentence):
    tree = analyzer.parse(sentence)
    chunks = []
    for chunk in tree.chunks:
        chunks.append(chunk.surface)
    return " ".join(chunks)


def read_file(file_path):
    with open(file_path) as f:
        return f.readlines()


def write_to_file(file_name):
    lines_array = read_file(file_name)
    processed_subtitle = seq(lines_array) \
        .filter(lambda x: x.startswith("Dialogue:")) \
        .map(lambda x: x.split(": ")[1]) \
        .map(lambda x: x.split(",")) \
        .filter(lambda x: x[3] == "白熊中文" or x[3] == "白熊日文") \
        .map(lambda x: (x[1], (x[3], x[9].strip()))) \
        .filter(lambda x: len(x[1][1]) > 1) \
        .partition(lambda x: x[1][0] == "白熊日文")

    japanese_subtitle = dict(processed_subtitle[0])
    chinese_subtitle = dict(processed_subtitle[1])
    merge_subtitle = {}
    for k in japanese_subtitle.keys():
        chunks = parse_sentence(japanese_subtitle[k][1])
        merge_subtitle[k] = (chinese_subtitle.get(k, ('白熊中文', '#')), japanese_subtitle[k], ("chunks", chunks))

    file_object = open(file_name[:-3] + "subtitle", 'w')

    for k, v in merge_subtitle.items():
        print(k)
        file_object.write(v[0][1] + "\n")
        file_object.write(v[1][1] + "\n")
        file_object.write(v[2][1] + "\n")
        file_object.write("\n")
    file_object.close()


def convert_ass(file_name):
    lines_array = read_file(file_name)
    file_object = open(file_name[:-4] + " chunks.ass", 'w')
    for line in lines_array:
        if line.startswith("Dialogue:") and line.split(",")[3] == "白熊日文":
            split_info = line.split(",")
            chunks_japanese = parse_sentence(split_info[-1].strip())+"\n"
            drop_last = split_info[0:-1]
            drop_last.append(chunks_japanese)
            file_object.write(",".join(drop_last))
        else:
            file_object.write(line)
    file_object.close()


if __name__ == '__main__':
    # print(sys.argv)
    # print(sys.argv[1])
    file = "/Users/daw/Downloads/[Kamigami] Shirokuma(Polar Bear) Cafe 01-50 [1280x720 x264 AAC MKV Sub(GB,BIG5,Jap)/[Kamigami] Shirokuma Cafe - 15 [1280x720 x264 AAC Sub(GB,BIG5,JP).ass"
    convert_ass(file)