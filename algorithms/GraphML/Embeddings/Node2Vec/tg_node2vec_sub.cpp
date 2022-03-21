 // node2vec function: given random walk sequence, this function trains vector using skip-gram model
 inline void tg_node2vec_sub(int dimension, string input_file, string output_file){
    Model model(dimension);
    model.sample_ = 0;
    // model.window = 10;
    int n_workers = 4;
    std::vector<SentenceP> sentences;

    size_t count =0;
    const size_t max_sentence_len = 200;

    SentenceP sentence(new Sentence);
    std::ifstream in(input_file);
    while (true) {
        std::string s;
        in >> s;
        if (s.empty()) break;
        ++count;
        sentence->tokens_.push_back(std::move(s));
        if (count == max_sentence_len) {
            count = 0;
            sentences.push_back(std::move(sentence));
            sentence.reset(new Sentence);
        }
    }

    if (!sentence->tokens_.empty())
        sentences.push_back(std::move(sentence));

    model.build_vocab(sentences);
    model.train(sentences, n_workers);
    model.save(output_file);

}
