#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    argv = dir(hidden_4)
    argc = len(dir(hidden_4))
    for i in range(argc):
        if argv[i][:2] != "__":
            print("{}".format(argv[i]))
