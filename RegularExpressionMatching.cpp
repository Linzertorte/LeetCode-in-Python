class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        return matchhere(p,s);
    }
    bool matchhere(const char *p,const char *s){
        if(*p=='\0') return *s=='\0';
        if(p[1]=='*') return matchstar(p[0],p+2,s);
        if(*s!='\0' && (*p=='.' || *p==*s)) return matchhere(p+1,s+1);
        return false;
    }
    bool matchstar(int c, const char *p, const char *s){
        do {
            
            if(matchhere(p,s)) return true;
        }while(*s!='\0' && (*s++ ==c || c=='.'));
        return false;
    }
};
