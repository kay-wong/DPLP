## extractparsing.py
## Author: Yangfeng Ji
## Date: 02-10-2015
## Time-stamp: <yangfeng 09/25/2015 23:43:17>

from preprocess.xmlreader import reader, writer, combine
from os import listdir
from os.path import join, basename
import glob

def extract(fxml, opath):
    sentlist, constlist = reader(fxml)
    sentlist = combine(sentlist, constlist)
    fconll = fxml.replace(".xml", ".conll")
    fconll = opath+ "/"+fconll.split("/")[-1]
    writer(sentlist, fconll)


def main(rpath, opath):
    files = [join(rpath,fname) for fname in listdir(rpath) if fname.endswith(".xml")]
    outfiles = [basename(x) for x in glob.glob(opath+"/*")]
    errorf = opath+"/errorf.txt"
    #print(outfiles[:5])
    for fxml in files:
        ofle = fxml.replace(".xml", ".conll").split("/")[-1]
        #print(ofle)
        if ofle in outfiles:
            #print "{} Exists".format(ofle)
            pass
        else:
            print 'Processing file: {}'.format(fxml)
            try: 
                extract(fxml, opath)
            except Exception as e:
                print("Failed to process: {}".format(fxml))
                print(e)
                with open(errorf, 'a') as f:
                    f.write(fxml)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        main(rpath=sys.argv[1], opath=sys.argv[2])
    else:
        print "python convert.py data_path"
