export default function MicrophoneRecorder() {

  const startRecording = async () => {

    const stream =
      await navigator.mediaDevices.getUserMedia({
        audio: true
      });

    console.log("Recording started");
  };

  return (
    <button onClick={startRecording}>
      🎤 Record
    </button>
  );
}
