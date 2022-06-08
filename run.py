from screen_recorder import ScreenRecorder

if __name__ == '__main__':
    try:
        ScreenRecorder().run()
    except Exception as e:
        print(e)
