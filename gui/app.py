# gui/app.py

import threading
import PySimpleGUI as sg
from downloader.auth import get_drive_services
from downloader.manager import download_folder

def run_download(folder_id, output, threads, window):
    try:
        drive = get_drive_services()
        download_folder(drive, folder_id, output, threads)
        window.write_event_value('-DONE-', None)
    except Exception as e:
        window.write_event_value('-ERROR-', str(e))

def main():
    sg.theme('DarkBlue3')
    # sg.theme('Dark Blue 3')
    # sg.ChangeLookAndFeel('DarkAmber')

    layout = [
        [sg.Text('Folder ID or Link'), sg.Input(key='-ID-')],
        [sg.Text('Output Dir'), sg.Input(default_text='.', key='-OUT-'), sg.FolderBrowse()],
        [sg.Text('Threads'), sg.Spin(list(range(1,17)), initial_value=4, key='-THR-')],
        [sg.Button('Download'), sg.Button('Exit')],
        [sg.Multiline(size=(80,20), key='-LOG-', autoscroll=True, disabled=True)]
    ]

    #window = sg.Window('Google Drive Downloader', layout)

    window = sg.Window('Google Drive Downloader', layout, icon=None, finalize=False)


    while True:
        event, values = window.read(timeout=100)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Download':
            fid = values['-ID-'].split('/')[-1].split('?')[0]
            out = values['-OUT-']
            thr = int(values['-THR-'])
            window['-LOG-'].print(f"Starting download of {fid} to {out} with {thr} threads...\n")
            threading.Thread(target=run_download, args=(fid, out, thr, window), daemon=True).start()

        if event == '-ERROR-':
            window['-LOG-'].print(f"Error: {values[event]}\n")

        if event == '-DONE-':
            window['-LOG-'].print("Download complete!\n")

    window.close()

if __name__ == '__main__':
    main()
