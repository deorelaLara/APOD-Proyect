import unittest
from APOD_Implement import *
from APOD_Abs import *
from Photo import *
from APOD_Implement import getPicture, Nasa

# Implementamos la interfaz de la app en la clase mock
class MockAPOD(BiblioAPOD):
    #Manipulamos la informacion manual 
    def __init__(self):
        self.photo=None

    def getInfo(self, date, title, explanation, url, media_type):
        self.photo = Photo(date, title, explanation, url, media_type)


    def getPhoto(self, date, title, explanation, url, media_type):
        self.photo = Photo(date, title, explanation, url, media_type)
        return self.photo

    def getPhoto(self,biblioDict):
        self.photo = Photo(biblioDict['date'], biblioDict['title'], biblioDict['explanation'], biblioDict['url'], biblioDict['media_type'])
        return self.photo

    # Buscamos la info en la clase del mock y no en la funcion original del API
    def SearchPicture(self, date):
        return self.photo

class TestNasa(unittest.TestCase):

    def testGetPicture(self):

        expect={
                    'date' : '2020-01-01',
                    'title' : 'Betelgeuse Imagined',
                    'explanation' :'Why is Betelgeuse fading?  No one knows.  Betelgeuse, one of the brightest and most recognized stars in the night sky, is only half as bright as it used to be only five months ago.  Such variability is likely just  normal behavior for this famously variable supergiant, but the recent dimming has rekindled discussion on how long it may be before Betelgeuse does go supernova.  Known for its red color, Betelgeuse is one of the few stars to be resolved by modern telescopes, although only barely.  The featured artist\'s illustration imagines how Betelgeuse might look up close. Betelgeuse is thought to have a complex and tumultuous surface that frequently throws impressive flares.  Were it to replace the Sun (not recommended), its surface would extend out near the orbit of Jupiter, while gas plumes would bubble out past Neptune.  Since Betelgeuse is about 700 light years away, its eventual supernova will not endanger life on Earth even though its brightness may rival that of a full Moon.  Astronomers -- both amateur and professional -- will surely continue to monitor Betelgeuse as this new decade unfolds.    Free Presentation: APOD Editor to show best astronomy images of 2019 -- and the decade -- in NYC on January 3',
                    'url' : 'https://apod.nasa.gov/apod/image/2001/BetelgeuseImagined_EsoCalcada_960.jpg',
                    'media_type' : 'image',
        }
        input2=expect.copy()
        input2['date']='2020-01-011'
        input3=expect.copy()
        input3['title']='*'*201
        input3=expect.copy()
        input3['explanation']='*'*3001
        input4=expect.copy()
        input4['url']=''
        input5=expect.copy()
        input5['media_type']='video'

        tests =[
            {   'type':'Photo: Todo correcto',
                'input' : expect,
                'expect_out' :expect,               
            },
            {
                'type':'Photo: date incorrecto',
                'input' : input2,
                'expect_out' : 1,
                
            },
            {
                'type':'Photo: title incorrecto',
                'input' : input3,
                'expect_out' :1,
                
            },
            {
                'type':'Photo: explanation incorrecto',
                'input' : input4,
                'expect_out' :1,
                
            },
            {
                'type':'Photo: Media_type incorrecto',
                'input' : input5,
                'expect_out' :1,
                
            }
        ] 

                # SE USARA SEARCH_PICTURE ORIGINAL 

        url='https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP'
        for tc in tests:
            print(tc['type'])
            actual = getPicture(tc['input'])
            if actual != 1:
                actual={'date':actual.date, 'title':actual.title, 'explanation':actual.explanation, 'url' :actual.url, 'media_type' :actual.media_type}
            vs=tc['expect_out']
            self.assertEqual(vs, actual)





    def test_searchPicture(self):

        print("\ntest_searchPicture")
        expect= {   
                    'date' : '2020-01-01',
                    'explanation' :'Why is Betelgeuse fading?  No one knows.  Betelgeuse, one of the brightest and most recognized stars in the night sky, is only half as bright as it used to be only five months ago.  Such variability is likely just  normal behavior for this famously variable supergiant, but the recent dimming has rekindled discussion on how long it may be before Betelgeuse does go supernova.  Known for its red color, Betelgeuse is one of the few stars to be resolved by modern telescopes, although only barely.  The featured artist\'s illustration imagines how Betelgeuse might look up close. Betelgeuse is thought to have a complex and tumultuous surface that frequently throws impressive flares.  Were it to replace the Sun (not recommended), its surface would extend out near the orbit of Jupiter, while gas plumes would bubble out past Neptune.  Since Betelgeuse is about 700 light years away, its eventual supernova will not endanger life on Earth even though its brightness may rival that of a full Moon.  Astronomers -- both amateur and professional -- will surely continue to monitor Betelgeuse as this new decade unfolds.    Free Presentation: APOD Editor to show best astronomy images of 2019 -- and the decade -- in NYC on January 3',
                    'media_type' : 'image',
                    'title' : 'Betelgeuse Imagined',
                    'url' : 'https://apod.nasa.gov/apod/image/2001/BetelgeuseImagined_EsoCalcada_960.jpg',
                }


        tests =[ #date correcto
            {   'type':'Input: Todo correcto',
                'input' : "2020-01-01",
                'expect_out' :expect,
                
            },
            {
                #un string cualquiera
                'type':'Input: Un string cualquiera',
                'input' : "hola_Error",
                'expect_out' : 1,
                
            },
            {   #lognitud diferente a 10
                'type':'Input: longitud diferente a 10',
                'input' : "2020-01-012",
                'expect_out' :1,
            },
            # },
            {   #formato correcto pero sin resultados
            'type':'Input: longitud diferente a 10',
            'input' : "2023-01-012",
            'expect_out' :1,
            }
        ] 

        ## SE USARA SEARCH_PICTURE ORIGINAL 

        url='https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP'
        for tc in tests:
            biblio_mock = MockAPOD()
            sp=Nasa(url)  
            print(tc['type']) 
            actual = sp.SearchPicture(tc['input'])
            self.assertEqual(tc['expect_out'], actual)





if __name__=='__main__':
    unittest.main()