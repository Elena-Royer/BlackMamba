import tarfile
import os 
from tkinter.ttk    import *
from tkinter        import *
import time
#from BM_INSTALL     import commands as cmd
from tqdm import tqdm
from BM_INSTALL import scroll_bar
import shutil


def unzip_file(path, path_destination_folder,  main_root ): 
    new_path = path+"/BM_TAR/black-mamba-1.01.01-linux.tar.gz"
    _path_   = path+"/BM_TAR/"
    
    try:
        base_path = os.environ("_MEI9442", _path_)
    except Exception:
        base_path = ""
    os.path.join(_path_)
    
    _scroll_bar_, frame  = locked(main_root, path_destination_folder)
    
    style = Style()
    style.theme_use('clam')#'clam', default
    style.configure('red.Horizontal.TProgressbar',background='blue')

    progress = Progressbar(frame, length=180, orient= HORIZONTAL, mode='determinate', 
    style='red.Horizontal.TProgressbar')
    progress.place(x=0, y=0)
    
    tar         = tarfile.open(new_path, mode="r:gz")
    members     = tar.getmembers()
    N           = len(members)
    step        = 0 
    M           = N // 100 
    
    for i, member in enumerate(members):
        main_root.update_idletasks()
        tar.extract(member, path = path_destination_folder)
        if step == M:
            progress['value'] += 1
            step = 0 
        else:
            if i == N-1:
                progress['value'] += 1
                step = 0  
            else: pass
        time.sleep(0.001)
        L = Label(frame, text=str(i)+f"/{N}",width=15, font = ('Arial', 10, 'bold'),
                            foreground='black')
        L.place(x=190, y=0)
        _scroll_bar_.insert(0, member.name)
        step += 1
    tar.close()
    Label(frame, text="                     ", width=15, font = ('Arial', 10, 'bold'), background="white", 
    foreground='white').place(x=190, y=0)
    entree = Entry(frame,  font=('arial', 10, 'bold'), width=50) 
    entree.place(x=190, y=0, width = 70)
    entree.insert(0, '')
    entree.delete(0, END)
    entree.insert(0,'Done !')
    entree.config(state=DISABLED,bg='ivory')
    
    progress_bar(main_root)
    
    name = 'black_mamba_location'
    __new_path__    = path_destination_folder+f"/BM_INSTALL/{name}/"
    new_path        = __new_path__+"install.bm"
    os.mkdir(__new_path__)
    with open(new_path, "w") as f:
        f.write('Done')
    f.close()
    
    __new_path__src    = path_destination_folder+f"/BM_INST/{name}/path.bm"
    shutil.move(__new_path__src, __new_path__)
    
    shutil.rmtree(path_destination_folder+f"/BM_INST/")
        
def progress_bar( main_root ):
    FRAME0 = Frame(main_root, relief=RAISED, bd=4, width=400, height=50, bg='white')
    FRAME0.place(x=200, y=360)
    break_button = Button(FRAME0, text='cancel', state=NORMAL, width=10, relief=GROOVE, command= lambda : destroy_root(main_root))
    break_button.place(x=280, y=4)
    
def locked( main_root, path_destination_folder):
    height = 40 
    List = ['Select location']
    FRAME = Frame(main_root, relief=RAISED, bd=4, width=400, height=350, bg="white")
    FRAME.place(x=200, y=0)
    FRAME0 = Frame(main_root, relief=RAISED, bd=4, width=400, height=50, bg='white')
    FRAME0.place(x=200, y=360)
    
    frame0 = LabelFrame(FRAME, bd=5, width=400, height=height, relief=FLAT, text="BLACK MAMBA PROGRAMM INSTALLING",
                        font = ('calibri', 10, 'bold'), bg="white")
    frame0.place(x=0, y=0, height=150)
    frame1 = Frame(FRAME, bd=5, width=400, height=height, relief=FLAT, bg='white' )
    frame1.place(x=0, y=150, height=height, width=300)
    frame2 = Frame(FRAME, bd=5, width=400, height=height, relief=FLAT, bg='white' )
    frame2.place(x=0, y=190, height=height, width=300)
    frame3 = Frame(FRAME, bd=5, width=400, height=height, relief=FLAT, bg='white' )
    frame3.place(x=0, y=230, height=height, width=300)
    frame4 = Frame(FRAME, bd=5, width=400, height=height, relief=FLAT, bg='white' )
    frame4.place(x=0, y=270, height=height, width=300)
    
    _scrooll_bar_ = scroll_bar.scroll_bar(frame0, "")
    
    label1 = Button(frame1, text=List[0], state=DISABLED, font=('calibi', 10, 'bold', 'underline'),
                        foreground="blue", width=50, height=50, relief=GROOVE, anchor='w')
    label1.pack()
    
    label = Label(frame2, text="PATH", anchor="w")
    label.place(x=0, y=0, width=300, height=30)
    
    entree = Entry(frame2, font=('arial', 10, 'bold'), width=50) 
    entree.place(x=50, y=0, width=300, height=30)
    entree.insert(0, '')
    entree.delete(0, END)
    entree.insert(0, f"{path_destination_folder}")
    entree.config(state=DISABLED,bg='ivory')
    
    check_bnt_int = IntVar()
    check_bnt_int.set(1)

    check_bnt = Checkbutton(frame3, text='activation', variable=check_bnt_int, onvalue=1,offvalue=0, selectcolor='ivory', state=DISABLED) 
    check_bnt.place(x=0, y=0)
    
    install_btn = Button(FRAME0, text="install", state=DISABLED, width=9,  relief=GROOVE )
    install_btn.place(x=0, y=4)
    
    prev_btn = Button(FRAME0, text="previous", state=DISABLED, width=9,  relief=GROOVE )
    prev_btn.place(x=100, y=4)
    
    return _scrooll_bar_, frame4

def destroy_root(root):
    root.destroy()