from gensim.models import word2vec, Word2Vec
from collections import defaultdict
from sklearn.cluster import KMeans


# 分散表現の読み込み
model = Word2Vec.load('input/w2v.model')

# print(model)
# print('----------------------')

# 最大単語数の指定
# 単語のリスト作成
max_vocab = 1000
vocab = list(model.wv.key_to_index.keys())[:max_vocab]
# print(vocab)
# ['の', '、', 'に', 'を', 'が', '。', 'は', 'と', 'で', '年', '・', 'して', 'した', 'する', 'いる', 'さ', 'も', '研究', '「', '」', '知能', '）', '（', 'いう', '開発', '人工', '制御', 'や', 'AI', 'こと', 'から', '化', 'し', '代', 'ファジィ', '学習', 'れた', '技術', '計算', '人間', 'データ', '機', 'である', '問題', 'れて', '処理', 'より', 'れる', 'れ', '月', 'ディープラーニング', 'コンピュータ', '，', '的', '手法', '世界', 'システム', 'ブーム', '機械', 'これ', 'ある', '提唱', '理論', '知的', 'など', 'なった', 'もの', '的な', 'ニューラルネットワーク', '従来', '日本', '者', '情報', 'エキスパートシステム', 'ように', '分野', '流行', 'おいて', '1990', '大きな', 'よる', '的に', '『', '第', '実現', '2010', '家電', '推論', '成果', '次', '知識', 'この', '物', '行わ', 'せる', '』', 'ニューロファジィ', '言語', '性', '等', 'ような', '脳', '認識', '画像', '応用', 'ら', '製品', '工学', '(', 'られて', 'まで', '呼ば', '量', '白', '深層', 'ず', '多数', '2017', '専門', '専用', '限界', 'なる', 'また', '解決', '最初の', 'コンピューター', '記号', '現在', '関する', '環境', 'ない', 'ビッグデータ', '生成', 'できる']

vectors = [model.wv[word] for word in vocab]
# print(vectors)
# array([ 1.97799001e-02,  3.90142798e-02, -8.72581557e-04, -2.38289796e-02,
#         3.96725200e-02, -7.23766759e-02,  7.03870580e-02,  1.46702006e-01,
#        -7.51292109e-02, -6.80407733e-02, -3.49012241e-02, -1.04076989e-01,
#         7.49355182e-03,  6.37837574e-02,  3.54457237e-02, -3.59032154e-02,
#         1.33407488e-02, -7.40442611e-03, -1.39748370e-02, -1.44979328e-01,
#         5.43776453e-02,  1.29190814e-02,  8.53764731e-03, -1.80088375e-02,
#        -1.08959712e-02,  6.04048558e-03, -2.56585553e-02, -2.73896139e-02,
#        -4.89805453e-02,  1.42653715e-02,  5.41976728e-02, -2.77291797e-02,
#         4.83455211e-02, -9.89102721e-02, -3.76861617e-02,  8.27235579e-02,
#         4.22415733e-02, -1.63955316e-02, -6.54544309e-03, -6.20494857e-02,
#         1.35017885e-02, -3.80647853e-02, -3.41266990e-02, -2.17352565e-02,
#         3.79312672e-02, -1.37308668e-02, -3.97443585e-02, -1.92792639e-02,
#         2.69150697e-02,  3.44471894e-02,  1.72421113e-02, -6.92800432e-02,
#         7.67692132e-03, -8.39795030e-06, -1.94304939e-02,  3.49175408e-02,
#         1.62749365e-02, -5.00180013e-03, -3.53354923e-02,  4.04822007e-02,
#         2.64755748e-02, -1.45960860e-02,  2.05063205e-02,  1.80430133e-02,
#        -5.11905104e-02,  1.11133583e-01,  1.74724981e-02,  4.16922309e-02,
#        -7.78779462e-02,  7.88181052e-02, -3.14443484e-02,  5.72020486e-02,
#         4.29119319e-02, -1.38331028e-02,  5.74022457e-02, -1.23890247e-02,
#         2.60980371e-02,  3.51934172e-02, -2.49133483e-02,  9.66727920e-03,
#        -4.32229638e-02,  2.14572549e-02, -6.01849556e-02,  7.03653619e-02,
#        -4.47976179e-02, -3.57390544e-03,  8.30703676e-02,  3.39740515e-02,
#         6.96457103e-02,  2.33685169e-02,  9.85673219e-02,  3.48631926e-02,
#        -1.25303715e-02, -3.75092030e-04,  7.71627054e-02,  3.77141498e-02,
#         2.84674298e-02, -3.90073396e-02,  1.66137125e-02,  1.31558627e-02],
#       dtype=float32)]

# クラスタの数の指定
# k-meansモデルの作成
# クラスタリングの実行
n_clusters = 50
kmeans_model = KMeans(
    n_clusters=n_clusters, 
    verbose=1, 
    random_state=42, 
    n_jobs=-1
)
kmeans_model.fit(vectors)

# クラスタリング後の結果作成
cluster_labels = kmeans_model.labels_
cluster_to_words = defaultdict(list)
for cluster_id, word in zip(cluster_labels, vocab):
    cluster_to_words[cluster_id].append(word)

# 出力
for words in cluster_to_words.values():
    print(words[:10])

# ['の']
# ['、']
# ['に', 'は']
# ['を']
# ['が']
# ['。']
# ['と', '年']
# ['で']
# ['・', 'し', '学習', 'データ', 'れ', '月']
# ['して', 'さ', '制御']
# ['した', 'いる']
# ['する', '研究']
# ['も', '「', 'いう', '開発']
# ['」', 'ファジィ']
# ['知能', '（', '技術']
# ['）', '機', 'れて', 'なった', 'よる', '製品']
# ['人工']
# ['や', 'AI']
# ['こと', 'れる', '的な']
# ['から', '化', '代', 'れた', '計算', '手法', '提唱']
# ['人間', 'ブーム', 'もの']
# ['である', '家電']
# ['問題']
# ['処理', '2010', '物']
# ['より', '世界']
# ['ディープラーニング', '，']
# ['コンピュータ', '知的', 'できる']
# ['的', '機械', 'ある', '理論', '大きな']
# ['システム', '流行']
# ['これ', '日本', '的に']
# ['など', '情報', '行わ', 'せる']
# ['ニューラルネットワーク', 'エキスパートシステム', 'この', '量']
# ['従来', 'おいて', '次', '知識']
# ['者']
# ['ように', '1990']
# ['分野', '工学', '呼ば', 'ず']
# ['『']
# ['第', '推論']
# ['実現', '』', '画像', '(']
# ['成果', '2017']
# ['ニューロファジィ', 'なる', '関する']
# ['言語', '深層', '多数']
# ['性', '現在']
# ['等', 'ような', '脳', 'られて', '白']
# ['認識', '限界', 'ない']
# ['応用', '解決', '環境']
# ['ら', '専門', '専用', 'ビッグデータ']
# ['まで']
# ['また', '最初の', 'コンピューター']
# ['記号', '生成']
