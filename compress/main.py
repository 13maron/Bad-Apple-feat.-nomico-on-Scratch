# coding: utf-8 (maybe)
# おなじディレクトリにBad Apple!!.mp4を置くとcompressed.txtを生成してくれます。多分

import mp42jpg
import textize
import compress

def main():
    mp42jpg.conv()
    textize.textize()
    textize.join()
    compress.quantize()
    compress.compress()

if __name__ == "__main__":
  main()
