class String
  def slugize
    self.downcase.gsub(/[\s\.]/, '-').gsub(/[^\w\d\-]/, '')
  end
end
