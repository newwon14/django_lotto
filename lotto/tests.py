from django.test import TestCase
from lotto.models import  GuessNumbers
# Create your tests here.

class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name="Test numbers", text='selected numbers')
        g.generate()
        #g.lottos #-> 6개씩 5set 총 3개 숫자의 리스트의 str
        print(g.update_date)
        print(g.lottos)

        self.assertTrue(len(g.lottos)>20) #run test를 했을 때 OK라고 뜸 !
