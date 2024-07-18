# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import argparse
import sys

sys.path.append("../..")
from pycorrector import eval_sighan2015_by_model_batch


def main(args):
    if args.model == 'kenlm':
        from pycorrector import Corrector
        m = Corrector()
        eval_sighan2015_by_model_batch(m.correct_batch)
        # Sentence Level: acc:0.5409, precision:0.6532, recall:0.1492, f1:0.2429, cost time:295.07 s, total num: 1100
    elif args.model == 'macbert':
        from pycorrector import MacBertCorrector
        model = MacBertCorrector()
        eval_sighan2015_by_model_batch(model.correct_batch)
        # macbert:      Sentence Level: acc:0.7918, precision:0.8489, recall:0.7035, f1:0.7694, cost time:2.25 s, total num: 1100
        # pert-base:    Sentence Level: acc:0.7709, precision:0.7893, recall:0.7311, f1:0.7591, cost time:2.52 s, total num: 1100
        # pert-large:   Sentence Level: acc:0.7709, precision:0.7847, recall:0.7385, f1:0.7609, cost time:7.22 s, total num: 1100
    elif args.model == 'bartseq2seq':
        from transformers import BertTokenizerFast
        from textgen import BartSeq2SeqModel
        tokenizer = BertTokenizerFast.from_pretrained('shibing624/bart4csc-base-chinese')
        model = BartSeq2SeqModel(
            encoder_type='bart',
            encoder_decoder_type='bart',
            encoder_decoder_name='shibing624/bart4csc-base-chinese',
            tokenizer=tokenizer,
            args={"max_length": 128})
        eval_sighan2015_by_model_batch(model.predict)
        # Sentence Level: acc:0.6845, precision:0.6984, recall:0.6354, f1:0.6654
    elif args.model == 'seq2seq':
        from pycorrector import ConvSeq2SeqCorrector
        model = ConvSeq2SeqCorrector()
        eval_sighan2015_by_model_batch(model.correct_batch)
        # Sentence Level: acc:0.3909, precision:0.2803, recall:0.1492, f1:0.1947, cost time:219.50 s, total num: 1100
    elif args.model == 't5':
        from pycorrector import T5Corrector
        model = T5Corrector()
        eval_sighan2015_by_model_batch(model.correct_batch)
        # Sentence Level: acc:0.7582, precision:0.8321, recall:0.6390, f1:0.7229, cost time:26.36 s, total num: 1100
    elif args.model == 'deepcontext':
        from pycorrector import DeepContextCorrector
        model = DeepContextCorrector()
        eval_sighan2015_by_model_batch(model.correct_batch)
        # Sentence Level: acc:
    elif args.model == 'ernie_csc':
        from pycorrector import ErnieCscCorrector
        model = ErnieCscCorrector()
        eval_sighan2015_by_model_batch(model.correct_batch)
        # Sentence Level: acc:0.7491, precision:0.7623, recall:0.7145, f1:0.7376, cost time:3.03 s, total num: 1100
    elif args.model == 'chatglm':
        from pycorrector.gpt.gpt_corrector import GptCorrector
        model = GptCorrector()
        eval_sighan2015_by_model_batch(model.correct_batch)
        # chatglm3-6b-csc: Sentence Level: acc:0.5564, precision:0.5574, recall:0.4917, f1:0.5225, cost time:1572.49 s, total num: 1100
    elif args.model=="mucgec_bart":
        import sys
        sys.path.append("./")
        from pycorrector.mucgec_bart.mucgec_bart_corrector import MuCGECBartCorrector
        model = MuCGECBartCorrector()
        eval_sighan2015_by_model_batch(model.correct_batch)
        # 该数据集无法体现模型的能力, 表现高于正确标准答案
        # Sentence Level: acc:0.2645, precision:0.2442, recall:0.2339, f1:0.2389, cost time:346.37 s, total num: 1100
    else:
        raise ValueError('model name error.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='kenlm', help='which model to evaluate')
    args = parser.parse_args()
    main(args)
