file = open("./inputs/day5.txt", "r")
lines = file.readlines()

range_flag = False

sources = {}
range_map = {}

for i, line in enumerate(lines):
    if i == 0: 
        sources_temp = line.split(":")[1].strip().split(" ")
        for j, s in enumerate(sources_temp):
            for s2 in range(int(s), int(sources_temp[j+1])):
                sources[int(s2)] = False 
                
        #print(seeds)

    if len(line.split(":")) > 1:
        range_flag = True
        sources = {key: False for key in sources}    
    elif range_flag:
        ranges = line.strip().split(" ")
        
        if len(ranges) == 3:
            source = int(ranges[1])
            dest = int(ranges[0])
            loops = int(ranges[2])
            #print(line)
            #print(ranges)
            old_keys = []
            new_keys = []

            for nr in sources:
                if source <= nr and source + loops > nr and not sources[nr]:
                    print(nr)
                    print("---")
                    old_keys.append(nr)
                    
                    diff = dest - source
                    nr += diff
                    print(nr)
                    print("\n")
                    new_keys.append(nr)

            for k in old_keys:
                sources.pop(k)

            for k in new_keys:
                sources[k] = True

            print(sources)
            # for j in range(loops):
            #     if source + j in sources and not sources[source + j]:
            #         sources.pop(source + j)
            #         sources[dest + j] = True

                    # range_map[source + j] = dest + j
                    # sources[source + j] = True
                # print(f"{source + j} : {dest + j}")

answer = min(sources.keys())
print(answer)