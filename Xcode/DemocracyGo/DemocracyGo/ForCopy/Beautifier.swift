//
//  Beautifier.swift
//  DareYou
//
//  Created by S on 02.02.19.
//  Copyright © 2019 burgkart. All rights reserved.
//

import Foundation
import UIKit

struct Colors {
    static let textColor = UIColor(hexString: "#000000")
    static let background = UIColor(hexString: "#EDEDED")
    static let backgroundLayerAbove = UIColor(hexString: "#DDDDDD")
    static let textBackground = UIColor(hexString: "#E8E8E8")
    static let highlight = UIColor(hexString: "#AABB25")
    
}

extension UIButton {
    func beautify(){
        self.backgroundColor = Colors.backgroundLayerAbove
        self.tintColor = Colors.textColor
        self.layer.cornerRadius = 10
    }
    
    open override func awakeFromNib() {
        self.beautify()
    }
}

extension UINavigationController {
    func beautify(){
        self.navigationBar.layer.shadowColor = UIColor.black.cgColor
        self.navigationBar.layer.shadowOffset = CGSize(width: 0.0, height: 2.0)
        self.navigationBar.layer.shadowRadius = 5
        self.navigationBar.layer.shadowOpacity = 0.3
        self.navigationBar.layer.masksToBounds = false
        self.navigationBar.tintColor = Colors.textColor
        
        let textAttributes = [NSAttributedString.Key.foregroundColor: Colors.textColor]
        self.navigationBar.titleTextAttributes = textAttributes
        self.navigationBar.largeTitleTextAttributes = textAttributes
        
        self.navigationBar.barTintColor = Colors.backgroundLayerAbove;
    }
    
    open override func awakeFromNib() {
        self.beautify()
    }
}

extension UITableView {
    func beautify(){
        self.contentInset = UIEdgeInsets(top: 16,left: 0,bottom: 0,right: 0)
        self.backgroundColor = Colors.background
        self.separatorStyle = .none
        // Do not show unused cells (appended below the data cells)
        self.tableFooterView = UIView()
    }
    
    open override func awakeFromNib() {
        self.beautify()
    }
}

extension UITableViewCell {
    
    func beautify(){
        self.backgroundColor = UIColor.clear
    }
    
    open override func awakeFromNib() {
        self.beautify()
    }
}

extension UITextView {
    
    func beautify() {
        self.backgroundColor = Colors.textBackground
    }
    
    open override func awakeFromNib() {
        self.beautify()
    }
}

extension UIColor {
    
    convenience init(hexString : String) {
        var cString:String = hexString.trimmingCharacters(in: .whitespacesAndNewlines).uppercased()
        
        if (cString.hasPrefix("#")) {
            cString.remove(at: cString.startIndex)
        }
        
        if ((cString.count) != 6) {
            fatalError("The hexString is not in the correct format.")
        }
        
        var rgbValue:UInt32 = 0
        Scanner(string: cString).scanHexInt32(&rgbValue)
        
        self.init(red: CGFloat((rgbValue & 0xFF0000) >> 16) / 255.0,
                  green: CGFloat((rgbValue & 0x00FF00) >> 8) / 255.0,
                  blue: CGFloat(rgbValue & 0x0000FF) / 255.0,
                  alpha: CGFloat(1.0))
    }
}
