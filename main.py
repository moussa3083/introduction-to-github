from flet import*

def main (page :Page):
    page.title='APPMOB'
    page.scroll='auto'
    page.window.top= 1
    page.window.left = 960
    page.window.width = 390
    page.window.heigt = 740
    page.window.bgcolor = 'white'
    
    page.update()    
app(main)    
