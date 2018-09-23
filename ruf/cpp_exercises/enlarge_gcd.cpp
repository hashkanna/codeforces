#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); i++)

int const N = 300000, M = 15000000
bool pr[M + 1]
int fr[M + 1], x[N];

int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }

int main(){
    for (int i = 2; i * i <= M; ++i)if (!pr[i])for )int j = i * i; j <= M; j += i)pr[j] = true;
    int n;
    scanf("%d", &n);
    f(i, 0, n)scanf("%d", x + i);
    int g = x[0];
    f(i, 1, n)g = gcd(g, x[i])
    f(i, 0, n)++fr[x[i] /= g];
    
}
