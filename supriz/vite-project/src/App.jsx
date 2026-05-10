import React, { useState, useEffect, useRef } from 'react';
import { Heart } from 'lucide-react';
import './index.css';

// Timeline Data
const timelineData = [
  { id: 1, date: '26 Şubat', desc: 'Birbirimizi tanıdığımız, hikayemizin başladığı o güzel gün. İlk bakış, ilk merhaba.', img: 'WhatsApp Image 2026-05-09 at 20.54.22.jpeg' },
  { id: 2, date: '16 Mayıs', desc: '"Biz" olduğumuz, ellerimizin birleştiği o sihirli tarih.', img: 'WhatsApp Image 2026-05-09 at 20.54.23.jpeg' },
  { id: 3, date: 'En Güzel Anlar', desc: 'Beraber güldüğümüz, dünyayı unuttuğumuz o an.', img: 'WhatsApp Image 2026-05-09 at 20.54.22 (1).jpeg' },
  { id: 4, date: 'Hatıralarımız', desc: 'Birlikte biriktirdiğimiz sayısız güzel anıdan sadece biri.', img: 'WhatsApp Image 2026-05-09 at 20.54.23 (1).jpeg' },
  { id: 5, date: 'Sonsuz Huzur', desc: 'Gözlerine her baktığımda hissettiğim o tarifsiz huzur.', img: 'WhatsApp Image 2026-05-09 at 20.54.22 (2).jpeg' },
  { id: 6, date: 'O Tatlı Gülüşün', desc: 'Dünyamı aydınlatan, bana her şeyi unutturan tebessümün.', img: 'WhatsApp Image 2026-05-09 at 20.54.23 (2).jpeg' },
  { id: 7, date: 'İlk Günki Gibi', desc: 'Sana olan aşkım her geçen gün sadece daha da büyüyor.', img: 'WhatsApp Image 2026-05-09 at 20.54.22 (3).jpeg' },
  { id: 8, date: 'Birlikte Öğrenmek', desc: 'Seninle deneyimlediğim her şey hayattaki en büyük şansım.', img: 'WhatsApp Image 2026-05-09 at 20.54.23 (3).jpeg' },
  { id: 9, date: 'Bizim Şarkımız', desc: 'Yan yanayken sessizliğin bile bana bir şarkı gibi gelmesi.', img: 'WhatsApp Image 2026-05-09 at 20.54.22 (4).jpeg' },
  { id: 10, date: 'Seninle Her Yer Güzel', desc: 'Mekanın hiçbir önemi yok, yeter ki elimi tut.', img: 'WhatsApp Image 2026-05-09 at 20.54.23 (4).jpeg' },
  { id: 11, date: 'Özel Anlar', desc: 'Kimsenin anlamadığı şakalarımıza birlikte kahkahalarla güldüğümüz o an.', img: 'WhatsApp Image 2026-05-09 at 20.54.22 (5).jpeg' },
  { id: 12, date: 'Saf Aşk', desc: 'Seni sadece sen olduğun için, her zerrenle sevmem.', img: 'WhatsApp Image 2026-05-09 at 20.54.23 (5).jpeg' },
  { id: 13, date: 'Geleceğimiz', desc: 'Seninle kurduğum hayallerin bile içimi ısıtması.', img: 'WhatsApp Image 2026-05-09 at 20.54.22 (6).jpeg' },
  { id: 14, date: 'Güven Limanım', desc: 'Kötü bir günün ardından sığındığım tek ve en güzel liman.', img: 'WhatsApp Image 2026-05-09 at 20.54.23 (6).jpeg' },
  { id: 15, date: 'Mucizem', desc: 'Hayatımdaki en değerli varlığım, benim küçük mucizem.', img: 'WhatsApp Image 2026-05-09 at 20.54.22 (7).jpeg' },
  { id: 16, date: 'Sonsuza Dek', desc: 'Bu hikayenin hiçbir zaman bitmeyecek olması...', img: 'WhatsApp Image 2026-05-09 at 20.54.23 (7).jpeg' }
];

const reasons = [
  { id: 1, text: "Gülüşünle en kötü günümü bile aydınlatabildiğin için..." },
  { id: 2, text: "Bana her zaman kendimi dünyanın en şanslı insanı hissettirdiğin için..." },
  { id: 3, text: "Kalbinin o eşsiz güzelliği ve sonsuz merhameti için..." },
  { id: 4, text: "Benimle deliler gibi eğlenip, en komik anılarımızı yarattığın için..." },
  { id: 5, text: "Bana güvenmeyi ve sevilmeyi en saf haliyle hissettirdiğin için..." },
  { id: 6, text: "Sadece sen olduğun için, her şeyinle sen olduğun için..." }
];

const loveLetter = "sevgilim herşeyim hayatımın anlamı seni o kadar çok seviyorum ki bazen bunu sana hissettiremiyorum gibi geliyor, bunu sana nasıl anlatacağımı bilemediğimden. O kadar yoğun, o kadar derin yaşıyorum ki bunu... Bilmiyorum, belki bazen seni sıkıyor muyum, bazen üzüyorum, bazen sana sesim yükseliyor ama seni gerçekten çok seviyorum. Seni hep mutlu etmek istiyorum, ben gerçekten hep mutlu etmek istiyorum. Çünkü mutlu olunca o kadar güzel oluyorsun ki... Aslında yanlış anlama hep güzelsin, sen çok güzelsin. Annen o kadar güzel yetiştirmiş ki, o kadar güzel yetiştirmiş ki kusursuz bi şeye dönüşmüşsün. İyi ki hayatımdasın, iyi ki varsın aşkım benim. Seni o kadar çok seviyorum ki...";

function App() {
  const [isPlaying, setIsPlaying] = useState(false);
  const letterRef = useRef(null);



  useEffect(() => {
    // Intersection Observer for word fade-in
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const words = entry.target.querySelectorAll('.letter-word');
            words.forEach((word, index) => {
              setTimeout(() => {
                word.classList.add('visible');
              }, index * 80); // stagger effect
            });
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.2 }
    );

    if (letterRef.current) {
      observer.observe(letterRef.current);
    }
    return () => observer.disconnect();
  }, []);

  return (
    <>
      <div className="bg-noise"></div>
      
      {/* Hero Section */}
      <section className="hero">
        <h1 className="hero-message">
          Seninle başlayan<br />en güzel hikayem...
        </h1>
        {!isPlaying ? (
          <div style={{ cursor: 'pointer', textAlign: 'center' }} onClick={() => setIsPlaying(true)}>
            <Heart className="pulse-heart" size={32} />
            <p style={{ marginTop: '1rem', fontStyle: 'italic', fontSize: '0.9rem', color: 'var(--text-gray)' }}>Müziği başlatmak için kalbe dokun</p>
          </div>
        ) : (
          <div style={{ textAlign: 'center' }}>
            <Heart className="pulse-heart" size={32} fill="var(--blush-accent)" />
            <iframe 
              width="0" 
              height="0" 
              src="https://www.youtube.com/embed/yeUQ9mjVp4k?autoplay=1&loop=1&playlist=yeUQ9mjVp4k" 
              frameBorder="0" 
              allow="autoplay" 
              allowFullScreen
            ></iframe>
          </div>
        )}
      </section>

      {/* Timeline Section */}
      <section className="section-padding">
        <div className="timeline-container">
          <div className="timeline-line"></div>
          {timelineData.map((item) => (
            <div key={item.id} className="timeline-item">
              <div className="timeline-dot"></div>
              <div className="timeline-content">
                <img src={`/${encodeURI(item.img)}`} alt="Anı" className="timeline-photo" loading="lazy" />
                <h3 className="timeline-date">{item.date}</h3>
                <p className="timeline-desc">{item.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>



      {/* Reasons Section */}
      <section className="reasons-section">
        <h2 className="reasons-title">Seni Neden Seviyorum?</h2>
        <div className="reasons-grid">
          {reasons.map((reason) => (
            <div key={reason.id} className="reason-card">
              <div className="reason-card-inner">
                <div className="reason-card-front">
                  <span className="reason-number">Sebep #{reason.id}</span>
                  <span className="reason-front-text">Öğrenmek İçin Dokun</span>
                </div>
                <div className="reason-card-back">
                  <p className="reason-back-text">{reason.text}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Love Letter Section */}
      <section className="letter-section">
        <div className="letter-card" ref={letterRef}>
          <div className="letter-separator">—</div>
          <p className="letter-text">
            {loveLetter.split(' ').map((word, i) => (
              <span key={i} className="word-wrap">
                <span className="letter-word">{word}</span>
              </span>
            ))}
          </p>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
        <div className="footer-content">
          <span>Oğulcan</span>
          <Heart className="footer-heart" size={16} fill="currentColor" />
          <span>Senin İçin</span>
          <span style={{ marginLeft: '10px' }}>2026</span>
        </div>
      </footer>
    </>
  );
}

export default App;
