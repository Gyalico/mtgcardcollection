import pickle
import mtgsdk

from mtgsdk import Card


# ここから開始
print( "Hello, Python" ) 

# カード情報の取得（時間がかかる場合あり）
cards = Card.all()

# カードデータのbinを保存する
cardfile = open( 'allcarddata.bin', 'wb' )
pickle.dump( cards, cardfile )
cardfile.close()

# 処理完了
print( "Good-bye, Python" ) 


