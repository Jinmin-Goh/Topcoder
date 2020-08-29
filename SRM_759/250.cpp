// Contest No.: SRM759
// Problem No.: 250
// Solver:      JEMINI
// Date:        20200829

#include <cstring>
#include <iostream>
#include <cstdlib>
#include <list>
#include <array>
#include <atomic>
#include <algorithm>
#include <deque>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <valarray>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class EllysViewPoints {
    public:
    int getCount(int N, int M, vector <string> matrix) {
        int ans = 0, rowCnt = 0, colCnt = 0;
        for(int i = 0; i < N; i++) {
            bool flag = false;
            for(int j = 0; j < M; j++) {
                if(matrix[i][j] == '#') {
                    flag = true;
                    break;
                }
            }
            if(!flag) {
                rowCnt++;
            }
        }
        for(int i = 0; i < M; i++) {
            bool flag = false;
            for(int j = 0; j < N; j++) {
                if(matrix[j][i] == '#') {
                    flag = true;
                    break;
                }
            }
            if(!flag) {
                colCnt++;
            }
        }
        return rowCnt * colCnt; // RETURN_TYPE
    }
};