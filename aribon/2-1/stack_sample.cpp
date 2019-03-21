#include <stack>
#include <cstdio>

using namespace std;

int main(){
    stack<int> s;  // int型をデータとするスタック
    s.push(1);
    s.push(2);
    s.push(3);
    printf("%d\n", s.top());  // 3
    s.pop();                  // 一番上から取り除く {1,2,3} -> {1,2}
    printf("%d\n", s.top());  // 2
    s.pop();
    printf("%d\n", s.top());  // 1
    s.pop();
    return 0;
}