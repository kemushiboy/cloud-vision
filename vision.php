$path = '{demo-image.jpg}';
 
$result = curl_init();
// curl url
curl_setopt($result, CURLOPT_URL, "https://vision.googleapis.com/v1/images:annotate?key={先ほど作成したブラウザ キー}");
// post
curl_setopt($result,  CURLOPT_CUSTOMREQUEST, 'POST');
// --data-binary
curl_setopt($result, CURLOPT_BINARYTRANSFER, true);
// header
curl_setopt($result, CURLOPT_HTTPHEADER, array( "Content-Type: application/json" ));
// get response with text
curl_setopt($result, CURLOPT_RETURNTRANSFER, true);
// image file
$file_contents = base64_encode(file_get_contents($path));
$request = '{
            　"requests": [
              　{
                　"image": {
                  　"content": "'. $file_contents .'"
                   },
                   　"features": [
                     　{
                       　"type": "LABEL_DETECTION"
                        }
                     ]
            　　　}
              ]
}';
curl_setopt($result, CURLOPT_POSTFIELDS, $request);
 
// result
$response = curl_exec($result);