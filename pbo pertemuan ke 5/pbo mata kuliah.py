from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data jadwal mata kuliah (contoh sederhana)
jadwal = [
    {
        'id': 1,
        'mata_kuliah': ',
        'waktu': 'Senin, 08:00 - 10:00',
        'ruang': 'A101'
    },
    {
        'id': 2,
        'mata_kuliah': 'Fisika Dasar',
        'waktu': 'Selasa, 10:00 - 12:00',
        'ruang': 'B202'
    },
    {
        'id': 3,
        'mata_kuliah': 'Kimia Dasar',
        'waktu': 'Rabu, 14:00 - 16:00',
        'ruang': 'C303'
    }
]

# Halaman utama
@app.route('/')
def index():
    return render_template('jadwal.html', jadwal=jadwal)

# Form tambah jadwal
@app.route('/tambah', methods=['GET', 'POST'])
def tambah_jadwal():
    if request.method == 'POST':
        mata_kuliah = request.form['mata_kuliah']
        waktu = request.form['waktu']
        ruang = request.form['ruang']

        new_jadwal = {
            'id': len(jadwal) + 1,
            'mata_kuliah': mata_kuliah,
            'waktu': waktu,
            'ruang': ruang
        }

        jadwal.append(new_jadwal)
        return redirect(url_for('index'))

    return render_template('tambah_jadwal.html')

if __name__ == '__main__':
    app.run(debug=True)
Dalam contoh ini, kami menggunakan Flask untuk membuat aplikasi web sederhana. Kami memiliki tiga contoh jadwal mata kuliah yang disimpan dalam list jadwal. Aplikasi ini memiliki dua rute:

/: Menampilkan halaman utama dengan daftar jadwal mata kuliah.
/tambah: Menampilkan form untuk menambahkan jadwal mata kuliah baru. Jika formulir diisi dan diajukan, jadwal baru akan ditambahkan ke list jadwal.
Untuk menjalankan aplikasi ini, Anda perlu membuat file HTML untuk halaman jadwal.html dan tambah_jadwal.html agar aplikasi dapat menampilkan halaman yang sesuai. Anda juga perlu menghubungkan aplikasi ini dengan database sebenarnya dan mengimplementasikan fitur-fitur lainnya sesuai kebutuhan.





