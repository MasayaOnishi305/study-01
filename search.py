import csv
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=[["ねずこ"],["たんじろう"],["きょうじゅろう"],["ぎゆう"],["げんや"],["かなお"],["ぜんいつ"]]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    if word in source:
        print("{}が見つかりました".format(word))
    ### ここに検索ロジックを書く
    else:
        print("{}が見つかりませんでした".format(word))
        source.append([word])
        print(word+"を追加しました")

if __name__ == "__main__":
    search()

with open("stock.csv","w",newline="",encoding="UTF_8_sig") as f:
    writer = csv.writer(f) 
    writer.writerows(source) 
    f.close()
