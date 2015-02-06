#!/usr/bin/env python

import grepy

def main():
    print("file match:")
    print(grepy.fileMatch(
        "test.txt",
        "ROOT_RELEASE"
    ))
    print("directory grep:")
    print(grepy.grep(
        directory = ".",
        pattern   = "ROOT_RELEASE"
    ))

if __name__ == '__main__':
    main()
