#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from gensim.models import word2vec
import MeCab
import sys
import networkx
import simplejson as json

def NetworkJP():
    model = word2vec.Word2Vec.load('./model/jp_wiki')
    graph = networkx.DiGraph()
    wordList=[u'援軍',u'ありがたがる',u'上',u'枯',u'多発',u'刑訴',u'署員',u'はりだし',u'さけび',u'さけぶ',u'差し障る',u'さける',u'お隠れ',u'切り合い',u'援護',u'駐禁',u'兆候',u'悶死',u'重労働',u'掘',u'ひるま',u'ひるみ',u'出向く',u'ひるむ',u'許す',u'見習い',u'たたき台',u'置き場',u'受入れ',
    u'くいとめる',u'巻物',u'大事',u'嫌がらせ',u'女殺し',u'おいおい',u'金額',u'大便',u'とどめる',u'いかばかり',u'趣向',u'趣味',u'行き渡る',u'一纏め',u'大切',u'弾除け',u'単細胞',u'多数',u'雄々しい',u'捨て身',u'設備',u'悶絶',u'差しだす',u'したたか',u'深追い',u'御祝い',u'あらためる',u'置き傘',u'苦しめる',u'魔法使い',u'持ち帰れる',
    u'大学',u'設定',u'ごみ捨て',u'折り紙',u'押し倒し',u'押し倒す',u'駐米',u'気配り',u'聴き込み',u'下書き',
    u'設想',u'えらべる',u'危険',u'大枠',u'申し込める',u'宿',u'読み込み',u'申し込む',u'極めつけ',
    u'あげつらう',u'女々しく',u'多少',u'起き出し',u'幼い',u'涼しく',u'涼しげ',u'ひそひそ',u'踏みにじり',
    u'寄せ木',u'途方',u'多寡',u'書換え',u'困り果てる',u'湯飲み',u'踏んづけ',u'とりくみ',u'あらがう',u'精いっぱい',
    u'略す',u'見慣れ',u'むちむち',u'釣り場',u'多い',u'完全',u'ごった返し',u'気づき',u'朽ち果て',u'むさくるしい',
    u'取り交わす',u'明るい',u'明るく',u'祟る',u'脱字',u'怒鳴りつける',u'お子様',u'値切る',
    u'脱力',u'お花畑',u'みずみずしい',u'危ない',u'呆れ',u'渦巻く',u'お年玉',u'足踏み',u'天下分け目',
    u'飼い犬',u'大人気',u'子育て',u'なだめる',u'話し出す',u'正社員',u'日雇い',u'汚れ役',u'延びる',u'謝金',
    u'完成',u'暗幕',u'振り返る',u'立ち回り',u'弱々しく',u'弱々しい',u'動かす',u'たしなみ',u'骨抜き',u'祓い',
    u'隣合う',u'仕入れ',u'情けない',u'険しく',u'険しい',u'来い',u'完遂',u'抜け出せる',u'大みそか',
    u'耐え忍ぶ',u'対決',u'燻る',u'見なす',u'研ぎ澄ます',u'引合い',u'捨てる',u'うつぶせ',u'燃えさかる'
    ,u'かっこいい',u'のぼりつめる',u'男らしい',u'なにげなく',u'軽々と',u'言い争い',u'昼食',u'避けろ',u'後まわし',
    u'ほのめかす',u'気むずかしい',u'閉じる',u'躬王',u'なじみ',u'かりあげ',u'階段',u'自重',u'渡世人',
    u'乗れる',u'事切れる',u'静か',u'真っ逆さま',u'恩知らず',u'ひょうきん',
    u'丸まる',u'用心深く',
    u'伝書鳩',u'捨て石',u'旦那',u'情緒',u'逆恨み',u'自転車',u'細やか',u'刑期',u'情愛',u'食いつく',u'にぎり',
    u'日射し',u'はげます',u'止まれ',u'太く',u'不一致',u'持ち込む',u'引っこ抜く',u'うきうき',
    u'あごひげ',u'持ち去る',u'治せる',u'首脳',u'こんぶ',u'渡り鳥',u'引き金',u'刻み付ける',u'めそめそ',u'沖縄',
    u'無神経',u'花開く',u'感じとる',u'読書',u'横向き',u'うめこみ',u'酷い',u'遠慮なく',u'拝める',
    u'せせら笑い',u'茶',u'尖り',u'祝い',u'祝う',u'起きあがる',u'短い',u'やわらかい',u'握り潰し',u'跳ね上がる',
    u'差し金',u'人並み',u'打ち上げる',u'似合う',u'奉る',u'滅多に',u'引き起こす',u'居座る',u'当て逃げ',
    u'乱れる',u'封じ込め',u'八百長',u'剥げる',u'叫び声',u'祝日',u'吐き',u'あたたか',
    u'あたため',u'勝ち目',u'寿司',u'たずさわる',u'読み誤り',u'淫乱',u'乗り切る',u'塩',u'酷吏',
    u'卑しい',u'ぐらぐら',u'広路通',u'短篇',u'つまみあげ',u'しり込み',u'とうぶん',u'セックス',u'さとり',u'くすぐったい',
    u'たしなめる',u'しぼる',u'短文',u'たたきつける',u'乱心',u'言説',u'手形',u'ひろう',u'下級生',u'みごもり',
    u'全国一',u'色気',u'地球儀',u'爆乳',u'終わる',u'短調',u'すぐれ',u'引き連れる',u'金縛り',u'おたずね者',
    u'お寺',u'お宝',u'お守',u'ごちそうさま',u'ちょくせつ',u'うずくまる',u'水風呂',u'祀る',u'食い潰す',u'激しい',
    u'あわせる',u'兄さん',u'惨たらしく',u'手順',u'雪国',u'けいもう',u'酷評',u'屋敷',u'身なり',u'現在地',u'社民党',
    u'吉報',u'じゃじゃ馬',u'しみこむ',u'ねじり鉢巻',u'仕上がり',u'とんずら',u'絡み付く',u'飾り',u'襲いかかる',u'改まる',
    u'なで下ろす',u'わざとらしい',u'遊び人',u'乗りかえ',u'喋る',u'ふわり',u'映す',u'育つ',u'歌う',u'明治',u'抱き合う',u'つけ回す',u'ぎりぎり',u'更迭',u'逃げ回る',u'消える',u'日本経済新聞',u'取りこむ',u'朗報',u'かきあげ',u'包茎',u'育子',u'集める',u'仰々しい',u'あこがれる',u'乳離れ',u'かわいい',u'くたばれ',u'逆らう',u'もったいない',u'たどりつく',u'受けつける',u'締めくくる',u'天皇陛下',u'吹かす',u'町民',u'ぜんそく',u'いごこち',
    u'鎮まる',u'がんさく',u'完敗',u'詰めかける',u'呼び込む',u'激怒',u'激情',u'尊い',u'尊ぶ',u'担ぎ出す',u'板書',
    u'見破る',u'新聞紙',
    u'尊崇',u'学修',u'組織',u'途切れる',u'俗気',u'農産物',u'支特',u'謁見',u'遡る',u'飼う',u'登る',u'防げる',
    u'力こぶ',u'たまわる',
    u'面積',u'父親',u'煮えたぎる',u'脱着',u'虫の息',u'孕む',u'満ちる',u'切腹',u'巻きこむ',u'激増',u'もらす',
    u'脱衣',u'散る',u'逆さま',u'練る',u'シナトラ',u'窃盗',u'大いなる',u'お化け',u'底抜け',u'泊る',u'人文字',
    u'帯金',
    u'けなす',u'指切り',u'めぐりあい',u'焼け焦げ',u'乗り切れる',u'美味',u'よっしゃ',u'生かす',
    u'いやがらせ',u'否み',u'馴れ',u'含む',u'可愛く',u'受ける',u'つまんない',u'走り去る',u'人道',u'お釈迦様',
    u'脅かす',u'ぶちこわし',u'とり入れる',u'残り物',u'引き分け',u'格付',u'謝する',u'騙し',
    u'ご多忙',u'表示',u'置き換え',u'きせる',u'受け手',u'受け方',u'おいしい',u'取りまわし',u'滑る',u'折り込む',
    u'坊っちゃん',u'的外れ',u'表彰状',u'心掛け',u'にじみ出る',u'はげしい',u'引きあげ',u'登り詰める',u'すり抜ける',u'取りかかる',
    u'いんらん',u'重ねる',u'口説き落とす',u'断わる',u'話合い',u'芸歴',u'もちこたえ',u'入り込む',
    u'張り裂ける',u'歌舞伎',u'立てこもる',u'功績',u'ぺたぺた',u'つぶやく',u'芸人',u'知り合い',u'語り継ぐ',
    u'欠場',u'ヤクザ',u'うらめし',u'人死',u'執念深い',u'天使',u'鳴く',u'わいろ',u'もし',u'ほの暗い',u'切り捨て',
    u'いこじ',u'懲らしめる',u'じじい',u'言うまでもない',u'人事',u'さびれる',u'おどろおどろしく',u'図太い',u'尾びれ',
    u'ぷちどる',u'突っ走る',u'被り',u'欠点',u'暮らし',u'人形',u'取り扱い',u'ふれあえる',u'打ち砕く',u'立て直す',u'買う',
    u'汚らわしい',u'道ばた',u'打ち明ける',u'てこずる',u'暴れだす',u'ひじ打ち',u'知る',u'噛み付く',u'滅ぶ',u'怒る',
    u'プログラミング',u'やりがい',u'煎る',u'しょんぼり',u'物差し',u'強み',u'倒れる',u'引き継ぎ',u'飛び乗る',
    u'押し入る',u'もろい',u'食いつなぐ',u'動ける',u'物怖じ',u'犯行',u'砕く',u'遊び歩く',u'のし上がる',
    u'逃げまどう',u'夫人',u'老いる',u'知能',u'かぶる',u'たおす',u'たおる',u'おどろき',u'くじ運',u'すり身',u'砲弾',u'お参り',
    u'卑しめる',u'あだ名',u'仲人',u'拝め',u'うろ覚え',u'よごれ',u'広域',u'憎らしい',u'粗大ごみ',u'肩代わり',u'おわる',
    u'返る',u'治まる',u'食す',u'目安',u'冷やかし',u'取り引き',u'担ぐ',u'引き込む',
    u'青空',u'童心',u'絶景',u'はねあげ',u'せんめつ',u'落ち込む',u'決着',u'忍び寄る',u'くすぶる',u'見習う',
    u'読み込む',u'かき氷',u'食卓',u'仕分ける',u'こっくり',u'ちぎれる',u'なぞる',u'秘技',u'増す',u'抜ける',u'いじめる',
    u'かき混ぜる',u'神通力',u'すがすがしい',u'ぼける',u'振り払う',u'ごみ',u'ひもじい',u'説く',u'乗り回す',
    u'おちょこ',u'睨み合う',u'送れる',u'ビキニ',u'絶食',u'食肉',u'もどかしい',u'吊るせ',u'ねむる',u'潜める',
    u'押し寄せる',u'目薬',u'気構え',u'払う',u'熱帯魚',u'仲間入り',u'秘める',u'目茶苦茶',u'読み出し',u'泣きどころ',
    u'押しつぶす',u'秘境',u'誠心',u'批判',u'盲目',u'捉える',u'納まる',u'つかまる',u'焦げ付く',
    u'おかあさんといっしょ',u'飛びかかる',u'か細く',u'うようよ',u'引き延ばす',u'恨めしい',u'埋め込む',u'終',u'あたる',
    u'おむつ',u'板ばさみ',u'いいわけ',u'積もる',u'たまたま',u'冷ややか',u'生き抜く',u'食らわす',
    u'立ち会い',u'ふざける',u'さみだれ',u'がんばれ',u'美しく',u'尖る',u'のび太',u'漢方',u'権化',u'けが人',
    u'引く手あまた',u'見返り',u'給与',u'おめでたい',u'咎める',u'言い切る',u'かかる',u'しめくくる',u'償う',
    u'心づかい',u'救う',u'取りあう',u'腹立つ',u'亡くなる',u'やわらか',u'飲み干す',u'差し入れる',u'争い',
    u'争う',u'引き出し',u'書き初め',u'震え上がる',u'じゅうたん',u'初犯',u'脱退',
    u'暴力団',u'最上級',u'かまえる',u'師弟',u'売れ残り',u'暗号',u'見立て',u'問い',u'手洗い',u'すり減る',
    u'あやしい',u'追いやる',u'うつむく',u'とげとげしい',u'抑え込む',u'問い掛ける',u'ふれ合う',
    u'抜け出す',u'飛び越える',u'寒々しい',u'寄りかかる',u'橋場',u'踏み倒す',u'書き取り',u'しゃみせん',u'震わす',
    u'まぬがれる',u'ぴょんぴょん',u'やり返す',
    u'消火栓',u'新大陸',u'天下り',u'汚らしい',u'生肉',u'売り渡す',u'心強い',u'うかがう',
    u'売りさばく',u'枯れる',u'さばさば',u'凝る',u'海水浴',u'求む',u'追いつめる',u'学びとる',u'なぞり',u'郵政',
    u'挙げる',u'使い古し',u'噛み砕く',u'供え物',u'接点',u'押出し',u'抜きんでる',u'演技',u'媚び',u'あわい',
    u'揺らめく',u'生死',u'無理強い',u'はえぬき',u'ぜん息',u'読む',u'焼き飯',u'奇想天外',
    u'生む',u'喰らう',u'差し押え',u'ひまわり',u'しんどい',u'混じる',u'身ごもる',u'外交',u'雨漏り',u'出遅れる',
    u'替える',u'引き取る',u'引き締め',u'はなはだしい',u'名乗る',u'巻き付く',u'寝取り',u'差し支え',
    u'いいなずけ',u'兄ちゃん',u'一人暮し',u'呆れる',u'摘み取る',u'進捗',u'押し付け',u'閉店',u'切れ者',
    u'ずぶ濡れ',u'進撃',u'注意深い',u'切り取り',u'人付き合い',u'馴れ初め',u'殉ずる',u'豪傑',u'消防署',u'締め付け',
    u'徒歩',u'ゆるめる',u'つけ込む',u'よじ登り',u'笑いかける',u'つまみ出す',u'焼け死ぬ',u'鉄棒',u'ひっぱたく',
    u'短所',u'溶け込む',u'不景気',u'悪態',u'いとしい',u'強力粉',u'見込み',u'面倒くさい',u'落ちる',
    u'落ちろ',u'駆け引き',u'わがまま',u'惑う',u'面倒臭い',u'引き回す',u'狂信',u'昇級',
    u'突っつく',u'埋め立てる',u'向かい合わせ',u'離れ業',u'不動産',u'花京院',u'還る',u'切り崩し',u'突っかかる',u'生ぬるい',
    u'脅し取る',u'怒り狂う',u'立会う',u'やっかみ',u'絞り込み',u'いばらき',u'離れる',u'催し',u'門外漢',u'床',
    u'転がす',u'暑苦しい',u'ほどよく',u'待ち受ける',u'お爺さん',u'むつまじい',u'川遊び',u'怨む',u'力ずく',u'恩人',u'苦痛',
    u'喜び',u'追っかける',u'売り出す',u'痛めつけ',u'演じる',u'なりすます',u'従える',u'雄たけび',u'あやかる',
    u'ぶっ殺す',u'鳴らす',u'妬ましく',u'味わう',u'画く',u'秘',u'あぶりだす',u'くみ上げる',u'思い知る',u'ふりかける',
    u'おぼえる',u'放り込む',u'うわの空',u'釣る',u'戦略',u'手広く',u'にらみ合い',
    u'取り押さえ',u'あやつる',u'だまる',u'だます',u'起案',u'捕まえる',u'大きい',u'僧尼',u'売出し',u'恐がる',u'特急',u'支払う',
    u'果てしない',u'こころよく',u'ぎこちなく',u'くさい',u'ぱっつん',u'混ぜる',u'小さい',u'泣ける',u'勇気づけ',
    u'すくすくと',u'活きる',u'はじめる',u'かあさん',u'うまれる',u'いちゃつく',u'流れ弾',u'剣',u'柔肌',u'泣きわめく',
    u'ゆさぶる',u'すいか',u'どさくさ紛れ',u'入れ知恵',u'原宿',u'膨らます',u'上回る',u'空き巣',
    u'にらみ合う',u'せせら笑う',u'理不尽',u'使い込む',u'使い込み',u'持ち寄る',u'ひとめぼれ',u'果たし合い',u'きれい事',u'のめりこむ',u'みじん切り',
    u'背負う',u'酔っぱらう',u'気持ち良い',u'盛り上がる',u'連れ出す',u'告げ口',u'支出',u'しこり',u'よなよな',u'気高い',
    u'ほっぺ',u'待ち合わせ',u'うろたえる',u'折れ曲がる',u'もぎ取る',u'勝ち越し',u'打合わせ',u'共感',u'露呈',u'温める',
    u'劣る',u'嘘っぱち',u'ひねり出す',u'問いつめる',u'太り過ぎ',u'行き詰まる',u'よろける',u'のろま',u'送る',u'目潰し',
    u'言い残す',u'黙る',u'心不全',u'人道的',u'おもちゃ',u'興味深い',u'綱引き',u'犯罪',u'砲丸投げ',u'容量',
    u'ときどき',u'恥知らず',u'外れる',u'隠れる',u'悟る',u'霧隠れ',u'辛い',u'感じろ',u'感じる',u'もてあます',u'顧客',
    u'引っかける',u'言い逃れる',u'たんぱく質',u'吹く',u'能力',u'聞き入る',u'得る',u'狂わす',u'見守る',u'ざっくばらん',
    u'投げる',u'割り込む',
    u'握りつぶす',u'飲みもの',u'犯す',u'休み',u'嫉み',u'ぺろぺろ',u'操り',u'焼き付ける',u'ときめく',u'ときめき',
    u'七転び八起き',u'慣れ親しむ',u'見苦しい',u'見直す',u'無能',u'収入',u'活かす',u'おちる',u'見せかけ',u'はちみつ',u'身体',u'むしゃくしゃ',u'思い過ごし',u'固まる',u'燃え上がる',u'波乱万丈',u'ちんちん',u'刷る',u'はね返り',u'さがす',u'力一杯',u'お勤め',u'ねらいうち',u'千客万来',
    u'つまむ',u'談話',u'もんもん',
    u'楽しむ',u'とんがり',u'仲間割れ',u'脱毛',u'おっぱい',u'巨乳',u'柔らかい',u'丸い',u'寒い',u'楽しい',u'狭い',
    u'濡れ衣',u'寂しい',u'早い',u'卑猥',u'安い',u'果てる',u'ぽんこつ',u'四つん這い',u'見せる',
    u'前借り',u'椅子',u'座る',u'速い',
    u'新幹線',u'乗る',u'車',u'冷蔵庫',u'白い',u'牛乳',u'飲む',u'水',u'透明',u'空気',u'吸う',u'吐く',u'息',
    u'二酸化炭素',u'化学',u'ドワンゴ',u'カドカワ',u'角川',u'プログラム',u'アニメ',u'映画',u'ゲーム',u'実況',
    u'インターネット',u'警察',u'動画',u'爆笑',
    u'テレビ',u'エロ',u'メディア',u'任天堂',u'生放送',u'エンタメ',u'書籍',
    u'マンガ',u'日本テレビ',u'フジテレビ',u'TBS',u'NHK',u'テレビ東京',u'テレビ朝日',u'うんちく',u'採用',
    u'会長',u'天才',u'面接',u'音楽',u'サラリーマン',
    u'うんちく',u'解答',u'アンケート',u'問題',u'支持',u'チャンネル',u'小説',u'勢い',u'おそろしい',
    u'はてな',u'お茶',u'おもろない',u'乳首',u'刈る',u'短髪',u'相撲',u'責任',u'引退',u'楽天',u'天然',u'ラーメン',u'秘密']

    for x in wordList:
        graph.add_node(x)
    for x in wordList:
        for y in wordList:
            weight = pow(1 - model.similarity(x, y),2)
            graph.add_edge(x, y, weight=weight)
    json.dump(dict(nodes=[[n, graph.node[n]] for n in graph.nodes()],edges=[[u, v, graph[u][v]] for u,v in graph.edges()]),open('graphJP.json', 'w'), indent=2)

def NetworkEN():
    pass

NetworkJP()