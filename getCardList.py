import pickle
import mtgsdk

from mtgsdk import Card


# ��������J�n
print( "Hello, Python" ) 

# �J�[�h���̎擾�i���Ԃ�������ꍇ����j
cards = Card.all()

# �J�[�h�f�[�^��bin��ۑ�����
cardfile = open( 'allcarddata.bin', 'wb' )
pickle.dump( cards, cardfile )
cardfile.close()

# ��������
print( "Good-bye, Python" ) 


