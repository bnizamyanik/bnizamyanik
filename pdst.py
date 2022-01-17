import sys, os

def loadSeqs():

    buff = []
    seqs = []
    for line in open("GivenFasta.fasta.txt", 'r'):  "Txt dosyası içerisindeki satır sayısı kadar for döngüsü döndürülür"
        if line.startswith('>'):                    "satır > işareti içerirse if'in içerisine girilir"
            if buff:                                "buff listesi boş değil ise bu if'in içerisine girilir"
                seqs.append(''.join(buff))          "buff listesi içerisindeki elamanlar birleştirilerek seqs'in içerisine yazılır"
                buff = []                           "buff bir sonraki gen dizimi için boşaltırılır"
        else:                                       "eğer > işareti bulunmazsa else'in içerisine girilir"
            buff.append(line.upper().strip())       "satır buff listesi içerisine temiz bir şekilde yazılır "
    if buff:                                        "son sekans for döngüsü içerisinde seqs listesine eklenmediği için buff listesi kontrol edilerek seqs listesine buff listesi sayesinde eklenir"
        seqs.append(''.join(buff))
    return seqs

seqs = loadSeqs()

for seq1 in seqs:                                   # Compare each sequence to each other.
    values = []
    for seq2 in seqs:
        dist = sum(c1!=c2 for c1,c2 in zip(seq1,seq2))  "karşılaştırılan 2 sekansın karakterleri tuple olarak tutulur. c1 ve c2 sekansların karakterlerine verilen isimdir. bu karakter sayısı kadar for döngsü döner. aynı olamayn karakter tuplesi için 1 puan verilir. sum fonksiyonu ile bu puanlar toplanır. "
        pdist = dist / float(len(seq1))                 "elde edilen puanın o sekansın eleman sayısına bölünerek float bir değer elde edilir."
        values.append('%.6f'% (pdist) )                 "virgülden sonraki basamak sayısını belirlemek için formatlama kullanılır. elde edilen değer values listesine eklenir."
    print(' '.join(values))                             "values listesindeki uzaklık değerleri aralarında bir boşluk bırkılarak ekrana yazdırılır. values listesi bir sekansın kendi ve diğer sekanslara olan uzaklığını barındırı. matrix değildir."
