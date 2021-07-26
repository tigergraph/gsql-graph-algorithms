#include <iostream>
#include <Eigen/Dense>

using namespace Eigen:MatrixXd;
using namespace std;

int main() {
    MatrixXd IDim2(2,2);
    IDim2(0,0) = 1
    IDim2(0,1) = 0
    IDim2(1,0) = 0
    IDim2(1,1) = 1
    cout << "2 Dimensional Identity Matrix" << IDim2 << endl;

}