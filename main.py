"""
                                      
                                                    
██████╗ ███████╗███╗   ██╗██╗   ██╗ ██████╗  █████╗ ███████╗ █████╗ ███╗   ██╗    
██╔══██╗██╔════╝████╗  ██║██║   ██║██╔════╝ ██╔══██╗██╔════╝██╔══██╗████╗  ██║    
██████╔╝█████╗  ██╔██╗ ██║██║   ██║██║  ███╗███████║███████╗███████║██╔██╗ ██║    
██╔═══╝ ██╔══╝  ██║╚██╗██║██║   ██║██║   ██║██╔══██║╚════██║██╔══██║██║╚██╗██║    
██║     ███████╗██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║███████║██║  ██║██║ ╚████║    
╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝    
                                                                                  
██████╗ ██╗  ██╗███╗   ███╗███╗   ███╗████████╗  ██╗                              
██╔══██╗██║ ██╔╝████╗ ████║████╗ ████║╚══██╔══╝  ██║                              
██████╔╝█████╔╝ ██╔████╔██║██╔████╔██║   ██║     ██║                              
██╔═══╝ ██╔═██╗ ██║╚██╔╝██║██║╚██╔╝██║   ██║██   ██║                              
██║     ██║  ██╗██║ ╚═╝ ██║██║ ╚═╝ ██║   ██║╚█████╔╝                              
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝   ╚═╝ ╚════╝                               


"""


class Perkenalan:
    nama = "Faris Faikar Razannafi"
    prodi = "Teknik Informatika"
    jurusan = "Ilmu Komputer"
    fakultas = "FMIPA"
    universitas = "UNNES"

    def __init__(self):
        print("----------- Perkenalan -----------")
        print(f"Nama: {self.nama}")
        print(f"Prodi: {self.prodi}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Fakultas: {self.fakultas}")
        print(f"Universitas: {self.universitas}\n")


def print_list(x):
    for i in range(len(x)):
        print(x[i])
    print('')


class Hobi:
    list_hobi = [
        "- Programming",
        "- Bermain Alat Musik",
        "- Graphic Design",
        "- Video Editing",
        "- Games"
    ]

    def __init__(self):
        print("------------- Hobi ---------------")

        print_list(self.list_hobi)

        print("1) Programming:")
        print(Programming.deskripsi_hobi)
        print("-v-")
        print("Manfaat programming:")
        print_list(Programming.manfaat_programming)

        print("2) Bermain Alat Musik:")
        print(BermainAlatMusik.deskripsi_hobi)
        print("-v-")
        print("Manfaat bermain alat musik:")
        print_list(BermainAlatMusik.manfaat_bermain_alat_musik)

        print("3) Graphic Design")
        print(GraphicDesign.deskripsi_hobi)
        print("-v-")
        print("Manfaat graphic design:")
        print_list(GraphicDesign.manfaat_graphic_design)

        print("4) Video Editing")
        print(VideoEditing.deskripsi_hobi)
        print("-v-")
        print("Manfaat video editing:")
        print_list(VideoEditing.manfaat_video_editing)


class Programming:
    deskripsi_hobi = (
        "Saya suka membuat proyek-proyek " +
        "kecil menggunakan Python, C++, dan C#.")

    manfaat_programming = [
        "- Melatih skill untuk bekerja nantinya",
        "- Menambah wawasan tentang ilmu pemrograman",
        "- Melatih skill problem-solving"
    ]


class BermainAlatMusik:
    deskripsi_hobi = (
        "Saya suka bermain alat musik seperti " +
        "gitar, piano, bass, dan drum."
    )

    manfaat_bermain_alat_musik = [
        "- Mengisi waktu luang",
        "- Meningkatkan konsentrasi",
        "- Membuat olahraga lebih mudah"
    ]


class GraphicDesign:
    deskripsi_hobi = (
        "Saya bisa menggunakan Adobe Illustrator " +
        "untuk membuat poster, banner, feeds IG, dll."
    )

    manfaat_graphic_design = [
        "- Melatih skill graphic design",
        "- Berguna ketika mengerjakan tugas visual",
        "- Menambah estetika profil media sosial"
    ]


class VideoEditing:
    deskripsi_hobi = (
        "Saya bisa menggunakan Adobe Premier " +
        "untuk mengedit short film, music video, dll."
    )

    manfaat_video_editing = [
        "- Melatih skill video editing dan cinematography",
        "- Berguna ketika mengerjakan tugas video",
        "- Dapat menyampaikan pesan melalui audio visual"
    ]


class Games:
    deskripsi_hobi = (
        "Saya suka bermain games yang berbasis coop " +
        "dan terkadang dengan orang luar negeri."
    )

    manfaat_games = [
        "- Menghilangkan stress",
        "- Melatih kerjasama tim",
        "- Melatih skill Bahasa Inggris"
    ]


class CitaCita:
    cita_cita_saya_adalah = [
        "- Menjadi programmer",
        "- Membanggakan orang tua"
    ]

    def __init__(self):
        print("----------- Cita-Cita ------------")
        print_list(self.cita_cita_saya_adalah)


if __name__ == '__main__':
    Perkenalan()
    Hobi()
    CitaCita()


"""


████████╗███████╗██████╗ ██╗███╗   ███╗ █████╗ 
╚══██╔══╝██╔════╝██╔══██╗██║████╗ ████║██╔══██╗
   ██║   █████╗  ██████╔╝██║██╔████╔██║███████║
   ██║   ██╔══╝  ██╔══██╗██║██║╚██╔╝██║██╔══██║
   ██║   ███████╗██║  ██║██║██║ ╚═╝ ██║██║  ██║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
                                               
██╗  ██╗ █████╗ ███████╗██╗██╗  ██╗            
██║ ██╔╝██╔══██╗██╔════╝██║██║  ██║            
█████╔╝ ███████║███████╗██║███████║            
██╔═██╗ ██╔══██║╚════██║██║██╔══██║            
██║  ██╗██║  ██║███████║██║██║  ██║            
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝            
                                               

"""
