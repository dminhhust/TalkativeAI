import { useEffect, useRef } from "react";

export default function WebcamCapture() {

  const videoRef = useRef();

  useEffect(() => {

    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {

        videoRef.current.srcObject = stream;
      });

  }, []);

  return (
    <video
      ref={videoRef}
      autoPlay
      width="300"
    />
  );
}
