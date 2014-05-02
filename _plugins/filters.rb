module Jekyll
  module Filters
    def slugize(text)
      text.slugize
    end
    
    def format_date(date)
      "#{date.strftime('%B')} #{date.strftime('%d')}, #{date.strftime('%Y')}"
    end
    
    def length(obj)
      obj.length if obj.respond_to? :length
    end
  end
end
