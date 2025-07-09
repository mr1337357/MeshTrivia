import sys

class ini:
    def __init__(self,filename):
        self.segments = {}
        with open(filename,'r') as infile:
            segment = None
            self.segments[None]={}
            for line in infile:
                #trim comments: (we're naiive so you can't put # in your data sorry
                index = line.find('#')
                if index >= 0:
                    line = line[:index]
                else:
                    line = line[:-1]
                if len(line) < 1:
                    continue
                if line[0] == '[':
                    index = line.find(']')
                    if index < 0:
                        sys.stderr.write('malformed header in config\n')
                    else:
                        segment = line[1:index]
                        self.segments[segment]={}
                    
                line = line.split('=')
                if len(line) !=2:
                    continue
                self.segments[segment][line[0]] = line[1]

    def __getitem__(self,key):
        return self.segments[key]

    def __contains__(self,key):
        return key in self.segments


if __name__ == '__main__':
    file = sys.argv[1]
    print(file)
    inf = ini(file)
    for segment in inf.segments:
        print('[{}]'.format(segment))
        for key in inf[segment]:
            print('{}={}'.format(key,inf[segment][key]))