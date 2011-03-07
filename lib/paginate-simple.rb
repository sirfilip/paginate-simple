module PaginateSimple
    attr_accessor :current_page, :total, :per_page
  
    def config(args = {})
      args = { :per_page => 10 }.merge(args)
      self.current_page = args[:page]
      self.total = args[:total]
      @per_page = args[:per_page] 
    end
  
    def num_of_pages
      (total.to_f / per_page.to_f).ceil 
    end
    
    def has_next_page?
      current_page < num_of_pages
    end
    
    def has_previous_page?
      current_page > first_page
    end
    
    def first_page
      1
    end
    
    def last_page
      num_of_pages
    end
    
    def pages
      (first_page..last_page).to_a
    end
    
    def offset
      (current_page - 1) * per_page
    end
    
    def next_page
      has_next_page? ? current_page + 1 : nil
    end
    
    def previous_page
      has_previous_page? ? current_page - 1 : nil
    end
    
    def current_page=(page)
      raise TypeError, "The page must be an 'Integer' like object" if not page.respond_to? :to_i
      page = page.to_i
      raise ArgumentError, "The page must be greater than 1, #{page} given" if page < 1
      @current_page = page
    end
    
    def total=(total_results)
      raise ArgumentError if total_results < 0
      @total = total_results
    end

end