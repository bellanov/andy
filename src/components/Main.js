import React, { useEffect, useState } from "react";

function Main() {
  const [documentContent, setDocumentContent] = useState("");

  useEffect(() => {
    // Fetch and parse the marked document
    fetch("/path/to/marked/document")
      .then((response) => response.text())
      .then((data) => setDocumentContent(data));
  }, []);

  return (
    <main className="app-main">
      <div dangerouslySetInnerHTML={{ __html: documentContent }} />
    </main>
  );
}

export default Main;
