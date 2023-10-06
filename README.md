
# Gerçek Zamanlı Rakam Sınıflandırma ve Eğitilmiş Model

Bu projede, gerçek zamanlı rakam sınıflandırma yapabilen bir modelin eğitimi ve kullanımı için gerekli kodları bulacaksınız. Proje iki ana bölümden oluşuyor: model eğitimi ve gerçek zamanlı sınıflandırma. İhtiyaca göre her iki bölümün de ayrı ayrı kullanılabilir.

## Model Eğitimi

1. "myData" adlı bir dizin oluşturun ve her bir rakam sınıfı için ayrı bir alt dizin oluşturun. Örneğin, "myData" dizini altında "0", "1", "2", ..., "9" gibi alt dizinler olmalıdır.
2. Her bir rakam sınıfına ait görüntüleri ilgili alt dizinlere yerleştirin. Görüntülerin boyutu 32x32 piksel olmalıdır.
3. `train_test_split` yöntemiyle verilerinizi eğitim, test ve doğrulama kümelerine bölebilirsiniz.
4. Modeli eğitmeden önce verilerinizi ön işleme adımlarından geçirin. Özellikle, görüntüleri gri tonlamalı hale getirin, histogram eşitleme uygulayın ve normalleştirin.
5. Evrişimli sinir ağı (CNN) modelini tanımlayın ve eğitim verileriyle eğitin.
6. Eğitilen modeli bir dosyaya kaydedin (örneğin, "model_trained_new.p").

## Gerçek Zamanlı Sınıflandırma

1. "model_trained_new.p" adlı dosyayı projenizin dizinine yerleştirin.
2. OpenCV (`cv2`) kütüphanesini kullanarak bir video kaynağı açın veya bir web kamerasını etkinleştirin.
3. Her kareyi işleyerek görüntüyü modele verin ve sınıflandırma sonuçlarını görüntüleyin.
4. Sınıflandırma sonuçları belirli bir eşik değerini (örneğin, 0.7) aştığında sonucu ekranda görüntüleyin.
5. Görüntü işleme ve sınıflandırma için gereken ön işleme adımlarını unutmayın.

## Daha fazla proje için [websitemi ziyaret edin !](http://ayazaktas.netlify.app)

## Bağımlılıklar

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç duyarsınız:

- `opencv-python` (Kamera ve görüntü işleme için)
- `numpy` (Sayısal hesaplamalar için)
- `scikit-learn` (Veri bölme ve değerlendirme için)
- `matplotlib` (Sonuçları görselleştirmek için)
- `seaborn` (Sonuçları görselleştirmek için)
- `keras` (Derin öğrenme modeli için)


Gerekli bağımlılıkları kurmak için aşağıdaki komutları kullanabilirsiniz:

```bash
pip install opencv-python numpy scikit-learn matplotlib seaborn keras

