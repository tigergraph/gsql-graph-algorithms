// random function, generate a random value between 0 and 1
inline float random(){
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0, 1);
    return dis(gen);
}

// generate a int random value given a range
inline int random_range(int start, int end){
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(start, end);
    return dis(gen);

}
// generate a random value based on probability distribution
// For example: given {0.5,0.3,0.2}, this function will generate {0,1,2} based on its probability	
inline int random_distribution(ListAccum<float> p){
    std::vector<float> a = p.data_;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::discrete_distribution<> dis(a.begin(), a.end());
    return dis(gen);
}