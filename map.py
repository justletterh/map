import json
def get_map():
    f=open("map.json","r")
    o=json.load(f)
    f.close()
    return o
def all(d):
    d=d['all']
    o=["All ips:\n"]
    t=" "*4
    for k in d:
        v=d[k]
        if type(v)==str:
            o.append(f"{t}{k}: {v}\n")
        elif type(v)==list:
            o.append(f"{t}{k}:\n")
            for i in v:
                o.append(f"{t}{t}{i}\n")
    o.append("end")
    return ("".join(o)).replace("\nend","")
def subnet(d,key):
    d=d[key]
    o=[f"All ips in the subnet \"{key}\":\n"]
    t=" "*2
    for k in d:
        v=d[k]
        o.append(f"{t}{k}: {v}\n")
    o.append("end")
    return ("".join(o)).replace("\nend","")
def main():
    div="-"*75
    print(div+"\n")
    dat=get_map()
    print(all(dat))
    print(subnet(dat,"192.168.1.x"))
    print(subnet(dat,"192.168.2.x"))
    print("\n"+div)

main()