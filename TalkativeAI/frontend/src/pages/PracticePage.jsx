import ChatBox from "../components/ChatBox";
import WebcamCapture from "../components/WebcamCapture";
import MicrophoneRecorder from "../components/MicrophoneRecorder";

export default function PracticePage({ token, scenario }) {

  return (
    <div>

      <h2>Practice Mode: {scenario}</h2>

      <WebcamCapture />

      <MicrophoneRecorder />

      <ChatBox
        token={token}
        scenario={scenario}
      />

    </div>
  );
}
