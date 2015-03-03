import spi, gpio
from time import sleep

 # define some screen commands


ILI9341_RESET = 0x01
ILI9341_SLEEP_OUT= 0x11
ILI9341_GAMMA = 0x26
ILI9341_DISPLAY_OFF=	0x28
ILI9341_DISPLAY_ON =	0x29
ILI9341_COLUMN_ADDR =	0x2A
ILI9341_PAGE_ADDR = 	0x2B
ILI9341_GRAM =	0x2C
ILI9341_MAC =	0x36
ILI9341_PIXEL_FORMAT =	0x3A
ILI9341_WDB =	0x51
ILI9341_WCD =	0x53
ILI9341_RGB_INTERFACE =	0xB0
ILI9341_FRC =	0xB1
ILI9341_BPC =	0xB5
ILI9341_DFC =	0xB6
ILI9341_POWER1 =	0xC0
ILI9341_POWER2	= 0xC1
ILI9341_VCOM1 =	0xC5
ILI9341_VCOM2 =	0xC7
ILI9341_POWERA =	0xCB
ILI9341_POWERB	= 0xCF
ILI9341_PGAMMA	= 0xE0
ILI9341_NGAMMA	= 0xE1
ILI9341_DTCA	= 0xE8
ILI9341_DTCB =	0xEA
ILI9341_POWER_SEQ =	0xED
ILI9341_3GAMMA_EN =	0xF2
ILI9341_INTERFACE =	0xF6
ILI9341_PRC =	0xF7




rst = gpio.GPIO(gpio.PD12)
rs  = gpio.GPIO(gpio.PD13)
cs  = gpio.GPIO(gpio.PC2)

def reset():
    rst.low()
    sleep(100)
    rst.high()
    sleep(100)

def write_command(c):
    cs.low()
    rs.low()
    spi.write(c)
    cs.high()

def write_data(c):
    cs.low()
    rs.high()
    spi.write(c)
    cs.high()

def clear(c=0x0000):
    write_command(0x2C)
    for i in range(240*320):
        write_data(c)
        write_data(c)

def write_image(image):
    write_command(0x2C)
    cs.low()
    rs.high()
    spi.write(image)
    cs.high()

def set_curser_pos(x1,y1,x2,y2):
	write_command(ILI9341_COLUMN_ADDR)
	write_data(x1 >> 8)
	write_data(x1 & 0xFF)
	write_data(x2 >> 8)
	write_data(x2 & 0xFF)
	write_command(ILI9341_PAGE_ADDR)
	write_data(y1 >> 8)
	write_data(y1 & 0xFF)
	write_data(y2 >> 8)
	write_data(y2 & 0xFF)

def draw_pixel(x,y,colour):
	set_curser_pos(x, y, x, y)
	write_command(ILI9341_GRAM)
	write_data(colour >> 8)
	write_data(colour & 0xFF)

def init():
	#HW reset
	write_command(0x01) #reset LCD
	sleep (120)
	#LCD init sequence
	write_command(0xC1) #PowerA
	write_data(0x39)
	write_data(0x2C)
	write_data(0x00)
	write_data(0x34)
	write_data(0x02)
	write_command(ILI9341_POWERB)
	write_data(0x00)
	write_data(0xC1)
	write_data(0x30)
	write_command(ILI9341_DTCA)
	write_data(0x85)
	write_data(0x00)
	write_data(0x78)
	write_command(ILI9341_DTCB)
	write_data(0x00)
	write_data(0x00)
	write_command(ILI9341_POWER_SEQ)
	write_data(0x64)
	write_data(0x03)
	write_data(0x12)
	write_data(0x81)
	write_command(ILI9341_PRC)
	write_data(0x20)
	write_command(ILI9341_POWER1)
	write_data(0x23)
	write_command(ILI9341_POWER2)
	write_data(0x10)
	write_command(ILI9341_VCOM1)
	write_data(0x3E)
	write_data(0x28)
	write_command(ILI9341_VCOM2)
	write_data(0x86)
	write_command(ILI9341_MAC)
	write_data(0x48)
	write_command(ILI9341_PIXEL_FORMAT)
	write_data(0x55)
	write_command(ILI9341_FRC)
	write_data(0x00)
	write_data(0x18)
	write_command(ILI9341_DFC)
	write_data(0x08)
	write_data(0x82)
	write_data(0x27)
	write_command(ILI9341_3GAMMA_EN)
	write_data(0x00)
	write_command(ILI9341_COLUMN_ADDR)
	write_data(0x00)
	write_data(0x00)
	write_data(0x00)
	write_data(0xEF)
	write_command(ILI9341_PAGE_ADDR)
	write_data(0x00)
	write_data(0x00)
	write_data(0x01)
	write_data(0x3F)
	write_command(ILI9341_GAMMA)
	write_data(0x01)
	write_command(ILI9341_PGAMMA)
	write_data(0x0F)
	write_data(0x31)
	write_data(0x2B)
	write_data(0x0C)
	write_data(0x0E)
	write_data(0x08)
	write_data(0x4E)
	write_data(0xF1)
	write_data(0x37)
	write_data(0x07)
	write_data(0x10)
	write_data(0x03)
	write_data(0x0E)
	write_data(0x09)
	write_data(0x00)
	write_command(ILI9341_NGAMMA)
	write_data(0x00)
	write_data(0x0E)
	write_data(0x14)
	write_data(0x03)
	write_data(0x11)
	write_data(0x07)
	write_data(0x31)
	write_data(0xC1)
	write_data(0x48)
	write_data(0x08)
	write_data(0x0F)
	write_data(0x0C)
	write_data(0x31)
	write_data(0x36)
	write_data(0x0F)
	write_command(ILI9341_SLEEP_OUT)

	sleep(100)

	write_command(ILI9341_DISPLAY_ON)
	write_command(ILI9341_GRAM)
    
