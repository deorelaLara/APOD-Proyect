import unittest
from APOD_Implement import *
from APOD_Abs import *
from Photo import *
from APOD_Implement import getPicture

# Implementamos la interfaz de la app en la clase mock
class MockAPOD(BiblioAPOD):
    #Manipulamos la informacion manual 
    def getInfo(self, date):
        self.photo = Photo(date)
    # Buscamos la info en la clase del mock y no en la funcion original del API
    def SearchPicture(self, date):
        return self.photo

class TestNasa(unittest.TestCase):

    def test_photo(self):
        tests = (
            {
                'input' : "2020-01-01",
                'expect_out' : {
                    'date' : '2020-01-01',
                    'title' : 'Betelgeuse Imagined',
                    'explanation' :'Why is Betelgeuse fading? No one knows. Betelgeuse, one of the brightest and most recognized stars in the night sky, is only half as bright as it used to be only five months ago. Such variability is likely just normal behavior for this famously variable supergiant, but the recent dimming has rekindled discussion on how long it may be before Betelgeuse does go supernova.  Known for its red color, Betelgeuse is one of the few stars to be resolved by modern telescopes, although only barely. The featured artist\'s illustration imagines how Betelgeuse might look up close. Betelgeuse is thought to have a complex and tumultuous surface that frequently throws impressive flares.  Were it to replace the Sun (not recommended), its surface would extend out near the orbit of Jupiter, while gas plumes would bubble out past Neptune.  Since Betelgeuse is about 700 light years away, its eventual supernova will not endanger life on Earth even though its brightness may rival that of a full Moon.  Astronomers -- both amateur and professional -- will surely continue to monitor Betelgeuse as this new decade unfolds. Free Presentation: APOD Editor to show best astronomy images of 2019 -- and the decade -- in NYC on January 3 ',
                    'url' : 'https://apod.nasa.gov/apod/image/2001/BetelgeuseImagined_EsoCalcada_960.jpg',
                    'media-type' : 'image'
                }
            }
        )

        for tc in tests:
            biblio_mock = MockAPOD()
            biblio_mock.getInfo(tc['expect_out'])

            actual = getPicture(tc['input'], biblio_mock)
            self.assertEqual(tc['expect_out'], actual)

if __name__=='__main__':
    unittest.main()