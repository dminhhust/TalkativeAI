import { useState } from "react";
import { sendMessage } from "../api/api";

export default function ChatBox({ token, scenario }) {

  const [messages, setMessages] = useState([]);
  const [text, setText] = useState("");

  const send = async () => {

    const res = await sendMessage(
      {
        session_id: 1,
        message: text,
        scenario
      },
      token
    );

    setMessages([
      ...messages,
      { role: "user", text },
      { role: "ai", text: res.data.response }
    ]);

    setText("");
  };

  return (
    <div>

      <div>

        {messages.map((m, i) => (
          <p key={i}>
            <b>{m.role}:</b> {m.text}
          </p>
        ))}

      </div>

      <input
        value={text}
        onChange={(e) =>
          setText(e.target.value)
        }
      />

      <button onClick={send}>
        Send
      </button>

    </div>
  );
}
