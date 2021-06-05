#include <bits/stdc++.h>
using namespace std;


class Vector {
    private:
        vector<double> v;
    public:
        size_t size;
        Vector(size_t size=0) {
            this->size = size;
            this->v.resize(size);
        }

        double& operator[](const size_t i) {
            return this->v[i];
        }

        Vector& operator*=(const int a) {
            /* 各要素にaをかける */
            vector<double> res = this->v;
            for (size_t i=0; i<this->size; i++) {
                res[i] *= a;
            }
            this->v = res;
            return *this;
        }
        const Vector operator*(const int a) {
            return Vector(*this) *= a;
        }

        Vector& operator*=(const double a) {
            /* 各要素にaをかける */
            vector<double> res = this->v;
            for (size_t i=0; i<this->size; i++) {
                res[i] *= a;
            }
            this->v = res;
            return *this;
        }
        const Vector operator*(const double a) {
            return Vector(*this) *= a;
        }

        void print() {
            int len = 0;
            for (size_t i=0; i<this->size; i++) {
                string str = to_string(this->v[i]);
                len = max(len, (int)str.size());
            }

            printf("[");
            for (size_t i=0; i<this->size; i++) {
                printf("%*lf", len, this->v[i]);
                if (i!=this->size-1) printf(", ");
            }
            printf("]\n");
        }
};

void test(){
    Vector vec(3);
    vec[0] = 0;
    vec[1] = 1;
    vec[2] = 2;

    vec *= 2;
    vec.print();

    vec *= 2.1;
    vec.print();
}


int main(int argc, char const *argv[]){
    test();
    return 0;
}