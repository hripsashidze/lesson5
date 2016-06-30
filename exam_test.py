def file_stats():
    long=''
    for line in open("data.txt"):
        if len(line)>len(long):
            long = line
    print(len(long))
    return (line)
file_stats()