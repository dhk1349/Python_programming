from copy import deepcopy

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = list(deepcopy(dominoes))
        state = ""
        start = 0
        for idx, c in enumerate(dominoes):
            if c == '.':
                continue
                
            elif c == 'L':
                if state == 'L':  # L L
                    for i in range(start, idx):
                        ans[i]='L'
                    start = idx
                elif state == "":
                    for i in range(start, idx):
                        ans[i] = 'L'
                    state = 'L'
                    start = idx
                else:  # R L
                    num_dom = idx - start + 1
                    if num_dom % 2 == 0:
                        for i in range(start, start+int(num_dom//2)):
                            ans[i] = 'R'
                        for i in range(start+int(num_dom//2), idx):
                            ans[i] = 'L'
                    else: 
                        for i in range(start, start+int(num_dom//2)):
                            ans[i] = 'R'
                        for i in range(start+int(num_dom//2)+1, idx):
                            ans[i] = 'L'

                    state = 'L'
                    start = idx
                    
                    
            elif c == 'R':  
                if state == 'R':  # R R
                    for i in range(start, idx):
                        ans[i]='R'
                    start = idx
                # else:  # L R
                    
                state = 'R'
                start = idx
            
        if state == 'R':
            for i in range(start, len(ans)):
                ans[i]='R'
        return "".join(ans)
