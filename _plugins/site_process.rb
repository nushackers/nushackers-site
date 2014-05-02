require 'growl'

module Jekyll
  class Site
    def process
      self.reset
      self.read
      self.generate
      self.render
      
      # these must come after render
      self.generate_archives
      
      self.cleanup
      self.write
      
      # Growl
    end
  end
end
