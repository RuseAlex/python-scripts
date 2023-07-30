import PyPDF2
import pyttsx3
import sys
import argparse

def create_mp3(filename):
    pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
    speaker = pyttsx3.init()
    for page_num in range(pdfReader.numPages):
        text = pdfReader.getPage(page_num).extractText()
        speaker.say(text)
        speaker.runAndWait()
    speaker.stop()
    engine.save_to_file(text, "audio.mp3")
    engine.runAndWait()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--filename',nargs=1,required=True,help="Name of the pdf file to be turned into mp3")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    arg = parser.parse_args()
    create_mp3(arg.filename[0])