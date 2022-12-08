import os
import time
import sys


def remove_old_files(director):
    lista_dictionare = []  # aici am cate un dictionar pentru fiecare fisier, cu (id, path, last_accessed, size)
    id = 0
    for current_path, directories, files in os.walk(director):
        for f in files:
            fisier = os.path.join(current_path, f)
            dictionar_fisier = {"id": id, "path": "", "last_accessed": "", "size": 0}
            dictionar_fisier.update({"path": fisier})

            timp_accesat = os.path.getatime(fisier)
            timp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timp_accesat))
            dictionar_fisier.update({"last_accessed": str(timp)})

            stats = os.stat(fisier)
            size = stats.st_size
            if size < 1024:
                size_str = str(round(size, 1)) + ' bytes'
            elif size / 1024 / 1024 < 1:
                size /= 1024
                size_str = str(round(size, 1)) + ' KB'
            elif size / 1024 / 1024 / 1024 < 1:
                size /= (1024 * 1024)
                size_str = str(round(size, 1)) + ' MB'
            elif size / 1024 / 1024 / 1024 / 1024 < 1:
                size /= (1024 * 1024 * 1024)
                size_str = str(round(size, 1)) + ' GB'

            dictionar_fisier.update({"size": size_str})
            id += 1
            lista_dictionare.append(dictionar_fisier)

    lista_dictionare.sort(key=lambda x: time.mktime(time.strptime(x["last_accessed"], '%Y-%m-%d %H:%M:%S')))

    top_ids = []
    print("Top 10 fisiere care au fost accesate cu cel mai mult timp in urma sunt: ")
    print()
    for i in range(0, 10):
        top_ids.append(lista_dictionare[i]["id"])
        print(lista_dictionare[i])
    print()
    print("Introduceti pe rand id-ul fisierelor de mai sus pe care doriti sa le stergeti.")
    print("Daca nu mai doriti sa stergeti niciun fisier, tastati 'stop'.")

    ok = 1
    while ok:
        try:
            input_id = int(input())
            if input_id in top_ids:
                for i in range(0, 10):
                    if lista_dictionare[i]["id"] == input_id:
                        to_delete = lista_dictionare[i]["path"]
                        os.remove(to_delete)
                        print("Ati sters fisierul " + lista_dictionare[i]["path"])
            else:
                print("[ERROR] Id-ul introdus nu se alfa in lista de mai sus")
        except:
            ok = 0
            print("[ERROR] Nu ati introdus un id de tip int.")



#print(remove_old_files("D:\Lavinia\FII3\Sem1\Python\Proiect"))

if __name__ == "__main__":
    director = str(sys.argv[1])
    remove_old_files(director)



