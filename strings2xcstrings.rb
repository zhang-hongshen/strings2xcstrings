class strings2xcstrings < Formula
  desc "Convert localization files from .strings to .xcstrings"
  homepage "https://github.com/zhang-hongshen/strings2xcstrings"
  url "https://github.com/zhang-hongshen/strings2xcstrings/archive/0.1.tar.gz"
  sha256 "checksum"

  depends_on "python"

  def install
    libexec.install "strings2xcstrings.py"
    (bin/"strings2xcstrings").write <<~EOS
    #!/bin/bash
    exec "#{libexec}/strings2xcstrings.py" "$@"
    EOS
  end

  test do
    # 测试脚本是否正常工作的测试命令
    system "#{bin}/strings2xcstrings", "--version"
  end
end
