# TOOLS_CFLAGS	:= -Wstrict-prototypes -Wshadow -Wpointer-arith -Wcast-qual \
# 		   -Wcast-align -Wwrite-strings -Wnested-externs -Winline \
# 		   -W -Wundef -Wmissing-prototypes
# # CFLAGS  := -O3 -g

# CC=gcc
# CFLAGS=-g -c

# #
# # Programs
# #
# all:	gpioThru 

# # gpioToggle: gpioToggle.c beaglebone_gpio.h
# # 	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

# gpioThru:  gpioThru.c beaglebone_gpio.h
# 	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<


# # gpiommap: gpiommap.o
# # 	$(CC) $^ -o $@

# # gpiommap.o: gpiommap.c gpiommap.h
# # 	$(CC) $(CFLAGS) $< -o $@

# #
# # Objects
# #

# %.o: %.c
# 	$(CC) $(CFLAGS) $(TOOLS_CFLAGS) -c $< -o $@

# clean:
# 	rm gpioThru

# print:
# 	@echo LDFLAGS = $(LDFLAGS)

CC=gcc
CFLAGS=-g -c

gpioThru: gpioThru.o
	$(CC) $^ -o $@

gpioThru.o: gpioThru.c beaglebone_gpio.h
	$(CC) $(CFLAGS) $< -o $@
