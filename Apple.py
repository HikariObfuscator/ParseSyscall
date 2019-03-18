import re
import requests
import json
import os
if __name__ == '__main__':
    txt=requests.get("https://raw.githubusercontent.com/apple/darwin-xnu/master/bsd/kern/syscalls.master").text
    matches=re.findall(r"^(\d{1,4}).*?{\ .*?\ ([a-zA-Z_]*?) ?\(.*?}",txt,re.MULTILINE)
    x=dict()
    for (num,name) in matches:
        if name=="nosys" or name=="enosys":
            continue
        else:
            x[name]=num
    path=os.path.join(os.getcwd(),"Syscalls.json")
    json.dump(x,open(path,"w"), sort_keys=True, indent=4)
