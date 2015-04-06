class Solution {
public:
    bool isMatch(const char *s,const char *p){
        if(*p=='\0') return *s=='\0';
        if(p[1]=='*') return matchstar(p[0],p+2,s);
        if(*s!='\0' && (*p=='.' || *p==*s)) return isMatch(s+1,p+1);
        return false;
    }
    bool matchstar(int c, const char *p, const char *s){
        do {
            
            if(isMatch(s,p)) return true;
        }while(*s!='\0' && (*s++ ==c || c=='.'));
        return false;
    }
};
